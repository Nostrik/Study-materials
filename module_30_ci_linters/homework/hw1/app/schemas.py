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

    def __str__(self):
        info = f'{self.id} | {self.dish_name} | {self.cooking_time}\n' \
               f'{self.ingredient_list} | {self.number_of_views}'
        return info

    class Config:
        orm_mode = True
