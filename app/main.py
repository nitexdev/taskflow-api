import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import auth_router, projects, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskFlow API",
    description="A project & task management API for freelancers — projects, tasks, priorities, and deadlines.",
    version="1.0.0",
)

client_origin = os.getenv("CLIENT_ORIGIN", "*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[client_origin] if client_origin != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}
