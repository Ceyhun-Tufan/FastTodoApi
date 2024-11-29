from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from models import Todo
from schemas import TodoCreate, TodoUpdate


async def create_todo(db: AsyncSession, todo: TodoCreate) -> Todo:
    new_todo = Todo(**todo.model_dump())  # Todo'yu oluştur, description dahil.
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo


async def get_todos(db: AsyncSession):
    result = await db.execute(select(Todo))
    return result.scalars().all()


async def get_todo(db: AsyncSession, todo_id: int):
    try:
        result = await db.execute(select(Todo).where(Todo.id == todo_id))
        return result.scalar_one()
    except NoResultFound:
        return None


async def update_todo(db: AsyncSession, todo_id: int, todo_data: TodoUpdate):
    todo = await get_todo(db, todo_id)
    if not todo:
        return None
    for key, value in todo_data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)
    await db.commit()
    await db.refresh(todo)
    return todo


async def delete_todo(db: AsyncSession, todo_id: int):
    todo = await get_todo(db, todo_id)
    if not todo:
        return None
    await db.delete(todo)
    await db.commit()
    return todo
