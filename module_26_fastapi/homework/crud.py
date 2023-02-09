from sqlalchemy.orm import Session
import models
import schemas


def get_recipe_by_id(db: Session, rec_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == rec_id).first()

