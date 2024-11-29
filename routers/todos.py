from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession 
from database import get_db
import crud
from schemas import TodoBase,TodoCreate,TodoUpdate
router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# her istekte yeni session acarak db islemlerini yapıyoruz
@router.get("/",response_model=list[TodoBase])
async def get_todos(db: AsyncSession = Depends(get_db)) -> dict:
    todos = await crud.get_todos(db)
    return todos

@router.post("/create/",response_model=TodoBase)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)) -> TodoBase:
    created_todo = await crud.create_todo(db,todo)
    return created_todo


@router.get("/get/{todo_id}",response_model = TodoBase)
async def get_todo(todo_id:int, db: AsyncSession = Depends(get_db))->dict:
    got_todo = await crud.get_todo(db,todo_id)
    return got_todo

@router.delete("/delete/{todo_id}",response_model = TodoBase)
async def delete_todo(todo_id:int, db:AsyncSession = Depends(get_db))->dict:
    deleted_todo = await crud.delete_todo(db,todo_id)
    
    if deleted_todo is None:
        raise HTTPException(status_code=404,detail="Not found")

    return deleted_todo


@router.put("/update/{todo_id}",response_model = TodoBase)
async def update_todo(todo_id: int, todo_data: TodoUpdate,db: AsyncSession = Depends(get_db)):
    updated_todo = await crud.update_todo(db,todo_id,todo_data)
    if updated_todo is None:
        raise HTTPException(status_code=404,detail="Can't find the todo wanted to update")
    return updated_todo


