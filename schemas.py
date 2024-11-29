from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# serializer


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False

    class Config:
        orm_mode = True


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

    class Config:
        orm_mode = True

class TodoBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
