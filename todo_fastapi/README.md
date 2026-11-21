# Todo Management API

A beginner-friendly Todo CRUD API built with FastAPI, SQLAlchemy, Pydantic, and SQLite.

## 1. Requirements

- Python 3.10+
- pip

## 2. Setup on Windows

Open a terminal in this project folder:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Run the API

```powershell
uvicorn app.main:app --reload
```

Open:
- API home: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

The SQLite database file `todo.db` is created automatically in the project root when the app starts.

## 4. Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/todos/` | Create a todo |
| GET | `/todos/` | Get all todos |
| GET | `/todos/{todo_id}` | Get one todo |
| PUT | `/todos/{todo_id}` | Update a todo |
| PATCH | `/todos/{todo_id}` | partial a todo completed |
| DELETE | `/todos/{todo_id}` | Delete a todo |

## 5. Example create request

POST `/todos/`

```json
{
  "title": "Learn FastAPI",
  "description": "Practice CRUD operations"
}
```

## 6. Project structure

```text
todo_fastapi/
├── app/
│   ├── database/
│   │   └── connection.py
│   ├── models/
│   │   └── todo.py
│   ├── schemas/
│   │   └── todo.py
│   ├── crud/
│   │   └── todo.py
│   ├── routers/
│   │   └── todo.py
│   └── main.py
├── requirements.txt
└── README.md
```

Each package includes an `__init__.py` file.
