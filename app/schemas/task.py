from sqlmodel import SQLModel
from typing import Optional

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None


class TaskRead(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

