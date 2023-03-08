import json
from pprint import pprint
from flask import Flask, Response, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Coffee, user_obj_list, coffee_obj_list, objects
from sqlalchemy.dialects.postgresql import insert, TSVECTOR
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql.expression import cast, select
from loguru import logger


app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://admin:admin@postgres', echo=False)
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
    logger.info('database has been updated')


@app.route('/users', methods=['GET'])
def get_all_users():
    logger.debug('get all users')
    all_users = session.query(User).all()
    users_list = [user.to_json() for user in all_users]
    return jsonify(users_list)


@app.route('/users_by', methods=['GET'])
def get_users_by_country():
    country = request.args.get('country')
    logger.debug(f"country is {country}")
    users_by_country = session.query(User).filter(User.address["country"].as_string() == country).all()
    users_by_country_list = [users.to_json() for users in users_by_country]
    return jsonify(users_by_country_list)


@app.route("/users", methods=['POST'])
def add_user():
    new_user_name = request.form.get("user_name")
    new_user_address = request.form.get("user_address")
    logger.debug(f"user_name is {new_user_name} | user_address is {new_user_address}")
    insert_query = insert(User).values(
        name=new_user_name,
        address=json.dumps(new_user_address)
    )
    session.execute(insert_query)
    session.commit()
    return 'user added successful', 200


@app.route("/coffee_search_full", methods=['GET'])
def full_text_search():
    if len(request.args):
        coffee_name_search = request.args.get('search_coffee')
        logger.debug(f"search coffee name is {coffee_name_search}")
        query = session.query(Coffee).filter(Coffee.title.match(coffee_name_search)).all()
        logger.debug(f'query is {query}')
    else:
        query = session.query(Coffee).all()
    coffee_list = [coffee.to_json() for coffee in query]
    return jsonify(coffee_list)


if __name__ == "__main__":
    app.run(debug=True)
