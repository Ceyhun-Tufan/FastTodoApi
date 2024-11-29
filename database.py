from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DBUSER = os.getenv("DBUSER")
DBPASSWORD = os.getenv("DBPASSWORD")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+asyncpg://{DBUSER}:{DBPASSWORD}@localhost/{DBNAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base sınıfı (tüm modeller buradan türetilir)
Base = declarative_base()

# Dependency (Veritabanı oturumunu sağlayan fonksiyon)
async def get_db():
    async with async_session() as session:
        yield session


