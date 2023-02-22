from flask import Flask, Response
from sqlalchemy import Column, Integer, String, Float, \
    create_engine, Sequence, Identity, ForeignKey, delete
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://admin:admin@localhost')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def index():
    return Response("Test PASS"), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
