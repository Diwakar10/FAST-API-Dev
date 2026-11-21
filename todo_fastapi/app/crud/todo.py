from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def create_todo(db: Session, todo: TodoCreate):
    new_todo = Todo(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all_todos(db: Session):
    return db.query(Todo).order_by(Todo.id).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    existing_todo = get_todo_by_id(db, todo_id)
    if existing_todo is None:
        return None

    update_data = todo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_todo, key, value)

    db.commit()
    db.refresh(existing_todo)
    return existing_todo


def delete_todo(db: Session, todo_id: int):
    existing_todo = get_todo_by_id(db, todo_id)
    if existing_todo is None:
        return None

    db.delete(existing_todo)
    db.commit()
    return existing_todo
