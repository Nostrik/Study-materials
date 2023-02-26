from flask import Flask, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import objects, Base


app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://admin:admin@localhost')
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def index():
    return Response("Test PASS"), 200


@app.before_request
def before_request():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.bulk_save_objects(objects)
    session.commit()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
