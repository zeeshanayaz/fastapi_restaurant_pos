from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.api.deps import get_session
from app.schemas.task import TaskCreate, TaskRead
from app.schemas.response import Response
from app.crud.task import create_task, get_tasks, get_task_by_id


router = APIRouter(prefix="/task", tags=["Tasks"])

@router.post("/", response_model=Response[TaskRead])
def create_new_task(task: TaskCreate, db: Session = Depends(get_session)):
    created_task = create_task(db, task=task)

    return Response(
        status= True,
        message= "Tasks created successfully",
        data= created_task
    )


@router.get("/", response_model=Response[list[TaskRead]])
def fetch_tasks(db: Session = Depends(get_session)):
    tasks = get_tasks(db)
    return Response(
        status= True,
        message= "Tasks retrieved successfully",
        data= tasks
    )



@router.get("/{task_id}", response_model=Response[TaskRead])
def fetch_task_by_id(task_id: int, db: Session = Depends(get_session)):
    task = get_task_by_id(db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(
        status= True,
        message= "Task retrieved successfully",
        data= task
    )