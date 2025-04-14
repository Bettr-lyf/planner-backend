from fastapi import FastAPI
from routers import goals, reflections
from database import engine, Base

app = FastAPI(title="Daily Planner API")

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(goals.router, tags=["goals"])
app.include_router(reflections.router, tags=["reflections"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)