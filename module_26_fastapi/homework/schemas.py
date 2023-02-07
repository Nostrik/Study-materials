from pydantic import BaseModel


class BaseRecipe(BaseModel):
    dish_name: str
    cooking_time: str
    ingredient_list: str
    description: str
    number_of_views: int


class RecipeIn(BaseRecipe):
    ...


class RecipeOut(BaseRecipe):
    id: int

    class Config:
        orm_mode = True
