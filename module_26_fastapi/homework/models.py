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
