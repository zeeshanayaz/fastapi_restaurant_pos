from sqlmodel import SQLModel
from typing import Optional

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None

class TaskPartialUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TaskRead(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

