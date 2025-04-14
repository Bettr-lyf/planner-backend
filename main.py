
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# MongoDB connection
client = AsyncIOMotorClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client.planner_db

class Goal(BaseModel):
    title: str
    description: str
    type: str
    created_at: datetime = datetime.utcnow()

class Reflection(BaseModel):
    rating: int
    notes: str
    date: datetime = datetime.utcnow()

@app.get("/")
async def index(request: Request):
    goals = {
        'daily': await db.goals.find({'type': 'daily'}).to_list(length=None),
        'weekly': await db.goals.find({'type': 'weekly'}).to_list(length=None),
        'monthly': await db.goals.find({'type': 'monthly'}).to_list(length=None)
    }
    return templates.TemplateResponse("index.html", {"request": request, "goals": goals})

@app.get("/add-goal")
async def add_goal_form(request: Request):
    return templates.TemplateResponse("add_goal.html", {"request": request})

@app.post("/add-goal")
async def add_goal(
    title: str = Form(...),
    description: str = Form(...),
    type: str = Form(...)
):
    goal = Goal(title=title, description=description, type=type)
    await db.goals.insert_one(goal.dict())
    return RedirectResponse(url="/", status_code=303)

@app.get("/reflect")
async def reflect_form(request: Request):
    return templates.TemplateResponse("reflect.html", {"request": request})

@app.post("/reflect")
async def reflect(
    rating: int = Form(...),
    notes: str = Form(...)
):
    reflection = Reflection(rating=rating, notes=notes)
    await db.reflections.insert_one(reflection.dict())
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
