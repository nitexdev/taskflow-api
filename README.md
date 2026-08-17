# TaskFlow API

A project & task management REST API for freelancers — projects, tasks, priorities, and deadlines. Built with FastAPI, which auto-generates interactive Swagger documentation at `/docs`, so anyone can explore and test every endpoint straight from the browser.

Live at : https://taskflow-api-vnzr.onrender.com/docs

<img width="4476" height="4252" alt="taskflow-api-vnzr onrender com_docs" src="https://github.com/user-attachments/assets/447d913f-fd30-45e9-83b6-e73d43905458" />


## Stack

FastAPI, SQLAlchemy, PostgreSQL, JWT auth (`python-jose`), `passlib`/`bcrypt` for password hashing.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/auth/register` | Create account, returns JWT |
| POST | `/auth/login` | Returns JWT |
| GET | `/projects` | List your projects |
| POST | `/projects` | Create a project |
| PUT | `/projects/{id}` | Update a project |
| DELETE | `/projects/{id}` | Delete a project |
| GET | `/tasks` | List tasks (filter by `?project_id=`, `?status=`) |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |
| GET | `/health` | Health check |

All routes except auth and health require `Authorization: Bearer <token>`. Full interactive docs at `/docs` (Swagger UI) and `/redoc`.

## Local setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # fill in DATABASE_URL and JWT_SECRET
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` to try it out. By default (no `DATABASE_URL` set), it falls back to a local SQLite file — fine for quick testing, but use Postgres for anything you want to persist or deploy.

## Deploying free

1. **Database — Neon** ([neon.tech](https://neon.tech)): free serverless Postgres. Create a project, copy the connection string (starts `postgresql://`).
2. **API — Render**: New → Web Service → connect this repo → root directory `taskflow-api` (or repo root if this is the whole repo). Render will detect `render.yaml` and use its build/start commands automatically. Add environment variables: `DATABASE_URL` (your Neon string), `JWT_SECRET` (long random string), `CLIENT_ORIGIN` (your frontend URL, or leave unset for `*` during testing).
3. Deploy, then visit `https://your-service.onrender.com/docs` to confirm it's live.

Free-tier note: Render's free web services sleep after 15 minutes idle — the first request after that takes ~30-50s to wake up.
