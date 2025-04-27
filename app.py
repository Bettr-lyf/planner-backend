from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from routes import task, auth
from contextlib import asynccontextmanager

from config.tortoise import init_db

bearer_scheme = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await init_db()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get('/health', tags=['health'])
def health():
  return {'message': 'All izz well!!'}

app.include_router(auth.router, prefix='/api/v1/auth', tags=['auth'])
app.include_router(task.router, prefix='/api/v1/tasks', tags=['tasks'], dependencies=[Depends(bearer_scheme)])