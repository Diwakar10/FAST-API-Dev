from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models.todo import Todo  # noqa: F401 - registers model metadata
from app.routers import todo

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo Management API",
    description="A beginner-friendly CRUD API using FastAPI and SQLAlchemy",
    version="1.0.0",
)

app.include_router(todo.router)


@app.get("/")
def home():
    return {"message": "Welcome to Todo Management API"}
