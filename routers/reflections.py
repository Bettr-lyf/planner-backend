
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from database import get_db
from models.reflection import Reflection
from schemas.reflection import ReflectionCreate, Reflection as ReflectionSchema

router = APIRouter()

@router.get("/reflections", response_model=List[ReflectionSchema])
async def list_reflections(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reflection))
    reflections = result.scalars().all()
    return reflections

@router.post("/reflections", response_model=ReflectionSchema, status_code=201)
async def create_reflection(reflection: ReflectionCreate, db: AsyncSession = Depends(get_db)):
    db_reflection = Reflection(**reflection.dict())
    db.add(db_reflection)
    await db.commit()
    await db.refresh(db_reflection)
    return db_reflection
