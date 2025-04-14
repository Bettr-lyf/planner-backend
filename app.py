from fastapi import FastAPI
from routes import task

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'Hello World'}

app.include_router(task.router, prefix='/api/v1/tasks', tags=['tasks'])