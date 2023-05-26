from typing import List
from fastapi import FastAPI
from sqlalchemy.future import select
from models import Base, Recipe
import schemas
from database import engine, session

app = FastAPI()


@app.on_event("startup")
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post('/recipe/', response_model=schemas.RecipeOut)
async def recipes(recipe: schemas.RecipeIn) -> Recipe:
    new_recipe = Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@app.get('/recipe/', response_model=List[schemas.RecipeOut])
async def recipes() -> List[Recipe]:
    async with session.begin():
        res = await session.execute(select(Recipe).order_by(Recipe.number_of_views.desc()))
    return res.scalars().all()


@app.get('/recipe/{idx}',  response_model=schemas.RecipeOut)
async def detail_recipe(idx: int) -> schemas.RecipeOut:
    async with session.begin():
        res = await session.execute(select(Recipe).filter(Recipe.id == idx))
        recipe = res.scalars().one()
        if res:
            recipe.number_of_views += 1
    return recipe
