from sqlmodel import Session, select
from app.models.task import Task
from app.schemas.task import TaskCreate


def create_task(db: Session, task: TaskCreate) -> Task:
    new_task = Task(title = task.title, description = task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session):
    return db.exec(select(Task)).all()


def get_task_by_id(db: Session, task_id: int) -> Task| None:
    return db.get(Task, task_id)