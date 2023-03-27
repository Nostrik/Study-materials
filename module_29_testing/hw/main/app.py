from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from typing import List
from loguru import logger
from datetime import datetime

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///prod.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .models import Client, Parking, ClientParking

    @app.before_request
    def before_request_func():
        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    @app.route("/test")
    def math_route():
        """Test route for check connection"""
        result = 'run successful'
        return jsonify(result)

    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        """Get all clients"""
        clients: List[Client] = db.session.query(Client).all()
        clients_list = [cl.to_json() for cl in clients]
        return jsonify(clients_list), 200

    @app.route("/clients/<int:client_id>", methods=['GET'])
    def get_client_by_id(client_id: int):
        """Get client by id"""
        client: Client = db.session.query(Client).get(client_id)
        return jsonify(client.to_json()), 200

    @app.route("/clients", methods=['POST'])
    def create_new_client():
        """Create new client"""
        name = request.form.get('name', type=str)
        surname = request.form.get('surname', type=str)
        credit_card = request.form.get('credit_card', type=str)

        new_client = Client(
            name=name,
            surname=surname,
            credit_card=credit_card
        )
        db.session.add(new_client)
        db.session.commit()
        return 'successful', 201

    @app.route("/parkings", methods=['POST'])
    def create_new_parking_zone():
        """Create new parking zone"""
        address = request.form.get('address', type=str)
        opened = request.form.get('opened', type=bool)
        count_places = request.form.get('count_places', type=int)
        count_available_places = request.form.get('count_available_places', type=int)

        new_parking_zone = Parking(
            address=address,
            opened=opened,
            count_places=count_places,
            count_available_places=count_available_places
        )
        db.session.add(new_parking_zone)
        db.session.commit()
        return 'successful', 201

    @app.route("/client_parkings", methods=['POST'])
    def parking_entrance():
        """Parking entrance"""
        client_id = request.form.get('client_id', type=int)
        parking_id = request.form.get('parking_id', type=int)
        logger.debug(f'client_id - {client_id}, parking_id - {parking_id}')
        time_in = datetime.now()
        current_parking: Parking = db.session.query(Parking).get(parking_id)
        count_available_places = current_parking.count_available_places
        parking_status = current_parking.opened

        if count_available_places <= 0 or not parking_status:
            return 'This parking is not available', 400

        new_client_parking = ClientParking(
            client_id=client_id,
            parking_id=parking_id,
            time_in=time_in
        )

        current_parking.count_available_places -= 1
        db.session.add(new_client_parking)
        db.session.commit()

        return '', 201

    @app.route("/client_parkings", methods=['DELETE'])
    def exit_from_the_parking_lot():
        client_id = request.form.get('client_id')
        parking_id = request.form.get('parking_id')
        logger.debug(f'client_id - {client_id}, parking_id - {parking_id}')
        time_out = datetime.now()
        current_parking: Parking = db.session.query(Parking).get(parking_id)
        current_client: Client = db.session.query(Parking).get(client_id)

        if current_client.credit_card:
            current_client_parking: ClientParking = db.session.query(ClientParking).get(client_id)
            current_client_parking.time_out = time_out
            current_parking.count_available_places += 1
            return '', 201
        return 'credit card not linked', 500

    return app
