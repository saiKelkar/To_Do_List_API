from fastapi import FastAPI
from .routes import auth_routes, task_routes

app = FastAPI()

@app.get("/")
def root():
    return { "message": "API running" }

app.include_router(auth_routes.router)
app.include_router(task_routes.router)