from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from typing import List

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///prod.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .models import Client, Parking, ClientParking

