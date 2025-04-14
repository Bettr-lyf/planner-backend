
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from database import get_db
from models.goal import Goal
from schemas.goal import GoalCreate, Goal as GoalSchema

router = APIRouter()

@router.get("/goals", response_model=List[GoalSchema])
async def list_goals(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Goal))
    goals = result.scalars().all()
    return goals

@router.post("/goals", response_model=GoalSchema, status_code=201)
async def create_goal(goal: GoalCreate, db: AsyncSession = Depends(get_db)):
    db_goal = Goal(**goal.dict())
    db.add(db_goal)
    await db.commit()
    await db.refresh(db_goal)
    return db_goal
