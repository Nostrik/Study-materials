from typing import Any, List

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.future import select

from . import models, schemas
from .database import engine, session

app = FastAPI()

client = TestClient(app)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get("/")
async def read_main():
    return "Hello World"


@app.post("/recipe/", response_model=schemas.RecipeOut)
async def add_recipe(recipe: schemas.RecipeIn) -> models.Recipe:
    new_recipe = models.Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@app.get("/recipe/", response_model=List[schemas.RecipeOut])
async def recipes():
    async with session.begin():
        res = await session.execute(
            select(models.Recipe).order_by(models.Recipe.num_of_views.desc())
        )
    return res.scalars().all()


@app.get("/recipe/{idx}", response_model=schemas.RecipeOut)
async def detail_recipe(idx: int):
    async with session.begin():
        res: Any = await session.execute(
            select(models.Recipe).filter(models.Recipe.id == idx)
        )
        recipe = res.scalars().one()
        if res:
            recipe.num_of_views += 1
    return recipe
