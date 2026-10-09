# Learn REST API

A starter Django REST Framework project with a CRUD API for tasks. It uses SQLite for local development and runs at `http://localhost:8000`.

## Run locally

```powershell
cd learn
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

Open `http://localhost:8000/api/tasks/` for the browsable API. The admin is at `http://localhost:8000/admin/`.

## Task endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/tasks/` | List tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/{id}/` | Retrieve a task |
| PUT/PATCH | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |

Example request body:

```json
{
  "title": "Learn Django REST Framework",
  "description": "Build my first API",
  "completed": false
}
```

This configuration is intended for local development. Set a private `SECRET_KEY`, configure production hosts, and disable `DEBUG` before deploying publicly.
