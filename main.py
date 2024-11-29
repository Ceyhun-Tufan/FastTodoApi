from fastapi import FastAPI
from routers import todos
from database import Base,engine


app = FastAPI()
app.include_router(todos.router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # Modelleri veritabanında oluştur
        await conn.run_sync(Base.metadata.create_all)

