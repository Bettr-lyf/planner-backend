from fastapi import FastAPI
from routes import task, auth
from contextlib import asynccontextmanager

from config.tortoise import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await init_db()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get('/')
def index():
  return {'message': 'Hello World'}

app.include_router(task.router, prefix='/api/v1/tasks', tags=['tasks'])
app.include_router(auth.router, prefix='/api/v1/auth', tags=['auth'])