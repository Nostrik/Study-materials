from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Float, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, mapper, declarative_base
from sqlalchemy import create_engine
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
engine = create_engine('sqlite:///homework.db')
Base = declarative_base()
Seesion = sessionmaker(bind=engine)
sesion = Seesion()


