import json
import logging
from typing import Tuple, List, Dict
from dataclasses import asdict
from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from models import (
    DATA,
    get_all_books,
    init_db,
    add_book,
    get_book_by_id,
    update_book_by_id,
    delete_book_by_id,
)
from schemas import BookSchema

app = Flask(__name__)
api = Api(app)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[routes]')


class BookList(Resource):
    def get(self) -> Tuple[List[Dict], int]:
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> Tuple[Dict, int]:

        data = request.json

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201


class Book(Resource):
    def get(self, book_id):
        answ = get_book_by_id(book_id)
        logger.debug(answ)
        return answ.__dict__, 201  # AttributeError, если запись не найдена

    def put(self, book_id):
        schema = BookSchema()
        data = request.json
        logger.debug(data)
        try:
            book = schema.load(data)  # как прикрутить book_id к data
        except ValidationError as er:
            return er.messages, 400
        ans = update_book_by_id(book)
        logger.debug(f'return is {ans}')
        return ans.__dict__, 201

    def delete(self, book_id):
        delete_book_by_id(book_id)
        return '', 204


api.add_resource(BookList, '/api/books')
api.add_resource(Book, '/api/books/<book_id>')


if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
