from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from loguru import logger
# from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, session, async_session

app = FastAPI()


# Dependency
# def get_db():
#     db = async_session()
#     try:
#         yield db
#     finally:
#         db.close()


@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.post('/recipe/', response_model=schemas.RecipeOut)
async def recipes(recipe: schemas.RecipeIn) -> models.Recipe:
    new_recipe = models.Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@app.get('/recipe/', response_model=List[schemas.RecipeOut])
async def recipes() -> List[models.Recipe]:
    res = await session.execute(select(models.Recipe))
    return res.scalars().all()


@app.get('/recipe/{idx}',  response_model=schemas.RecipeOut)
async def detail_recipe(idx: int):
    # res = await session.query(models.Recipe).filter(models.Recipe.id == idx).one_or_none()
    # res = crud.get_recipe_by_id(db, rec_id=idx)
    res = await session.execute(select(models.Recipe.id == idx))
    logger.debug(res)
