from flask import Flask, Response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import objects, Base, User, Coffee
from sqlalchemy.dialects.postgresql import insert
from loguru import logger


app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://admin:admin@postgres')
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def index():
    logger.debug('Test pass logger')
    return Response("Test PASS"), 200


@app.before_request
def before_request_func():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.bulk_save_objects(objects)
    session.commit()


# @app.route("/users", methods=['POST'])
# def add_user():
#     new_user_name = request.form.get("user_name")
#     new_user_address = request.form.get("user_address")
#     insert_query = insert(User).values(
#         name=new_user_name,
#         address=new_user_address
#     )


if __name__ == "__main__":
    app.run(debug=True)
