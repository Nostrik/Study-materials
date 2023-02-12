from typing import List
from fastapi import FastAPI
from sqlalchemy.future import select
from sqlalchemy import func
from loguru import logger
# import models
from . import models
import schemas
from . import database
# from database. import engine, session
from . import *
from fastapi.testclient import TestClient

app = FastAPI()


@app.on_event("startup")
async def shutdown():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await database.session.close()
    await database.engine.dispose()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post('/recipe/', response_model=schemas.RecipeOut)
async def recipes(recipe: schemas.RecipeIn) -> models.Recipe:
    new_recipe = models.Recipe(**recipe.dict())
    async with database.session.begin():
        database.session.add(new_recipe)
    return new_recipe


@app.get('/recipe/', response_model=List[schemas.RecipeOut])
async def recipes() -> List[models.Recipe]:
    async with database.session.begin():
        res = await database.session.execute(select(models.Recipe).order_by(models.Recipe.number_of_views.desc()))
    return res.scalars().all()


@app.get('/recipe/{idx}',  response_model=schemas.RecipeOut)
async def detail_recipe(idx: int) -> schemas.RecipeOut:
    async with database.session.begin():
        res = await database.session.execute(select(models.Recipe).filter(models.Recipe.id == idx))
        recipe = res.scalars().one()
        if res:
            recipe.number_of_views += 1
    return recipe
