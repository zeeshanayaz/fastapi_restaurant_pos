from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.api.v1.task import router as task_router
from app.schemas.response import Response

app = FastAPI(
    title="Restaurant POS API",
    description="API for managing restaurant point of sale operations",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get('/', response_model=Response)
def health_check():
    return Response(
        status= True,
        message= "API is running."
    )

app.include_router(task_router, prefix="/api/v1")


