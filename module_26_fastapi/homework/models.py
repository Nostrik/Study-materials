from sqlalchemy import Column, String, Integer

from database import Base


class Recipe(Base):
    __tablename__ = 'Recipe'
    id = Column(Integer, primary_key=True, index=True)
    dish_name = Column(String, index=True)
    cooking_time = Column(String, index=True)
    ingredient_list = Column(String, index=True)
    description = Column(String, index=True)
    number_of_views = Column(Integer, index=True)

    def __str__(self):
        info = f'{self.id} | {self.dish_name} | {self.cooking_time}\n' \
               f'{self.ingredient_list} | {self.number_of_views}'
        return info

    def increment_views(self):
        self.number_of_views += 1
