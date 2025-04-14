
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from datetime import datetime
import os
from dotenv import load_dotenv
from database import database, Goal, Reflection, init_db
from schemas import GoalCreate, ReflectionCreate

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def startup():
    await database.connect()
    init_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def index(request: Request):
    query = "SELECT * FROM goals ORDER BY created_at DESC"
    goals = await database.fetch_all(query)
    
    categorized_goals = {
        'daily': [g for g in goals if g['category'] == 'daily'],
        'weekly': [g for g in goals if g['category'] == 'weekly'],
        'monthly': [g for g in goals if g['category'] == 'monthly']
    }
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "goals": categorized_goals
    })

@app.get("/add-goal")
async def add_goal_form(request: Request):
    return templates.TemplateResponse("add_goal.html", {"request": request})

@app.post("/add-goal")
async def add_goal(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...)
):
    query = """
    INSERT INTO goals (title, description, category, created_at)
    VALUES (:title, :description, :category, :created_at)
    """
    values = {
        "title": title,
        "description": description,
        "category": category,
        "created_at": datetime.utcnow()
    }
    await database.execute(query=query, values=values)
    return RedirectResponse(url="/", status_code=303)

@app.get("/reflect")
async def reflect_form(request: Request):
    goals = await database.fetch_all("SELECT * FROM goals ORDER BY created_at DESC")
    return templates.TemplateResponse("reflect.html", {
        "request": request,
        "goals": goals
    })

@app.post("/reflect")
async def reflect(
    goal_id: int = Form(...),
    rating: int = Form(...),
    comment: str = Form(...)
):
    query = """
    INSERT INTO reflections (goal_id, rating, comment, created_at)
    VALUES (:goal_id, :rating, :comment, :created_at)
    """
    values = {
        "goal_id": goal_id,
        "rating": rating,
        "comment": comment,
        "created_at": datetime.utcnow()
    }
    await database.execute(query=query, values=values)
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
