from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import todo as todo_crud
from app.database.connection import get_db
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_crud.create_todo(db, todo)


@router.get("/", response_model=list[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    return todo_crud.get_all_todos(db)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_crud.get_todo_by_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
):
    updated_todo = todo_crud.update_todo(db, todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo


@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db)
):
    updated_todo = todo_crud.update_todo(db, todo_id, todo)

    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated_todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = todo_crud.delete_todo(db, todo_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully", "id": todo_id}
