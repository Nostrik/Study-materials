import logging
from typing import Tuple, List, Dict

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
    def get(self, b_id) -> Tuple[List[Dict], int]:
        logger.debug(b_id)
        schema = BookSchema()
        return schema.dump(get_book_by_id(b_id), many=True), 200

    def put(self, b_id) -> Tuple[Dict, int]:

        data = request.json
        logger.debug(data)

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = update_book_by_id(book)
        return schema.dump(book), 201

    def delete(self, b_id):
        delete_book_by_id(b_id)
        return '', 204


api.add_resource(BookList, '/api/books')
api.add_resource(Book, '/api/books/<id>')


if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
