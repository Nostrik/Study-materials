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
    add_author,
    get_book_by_id,
    update_book_by_id,
    delete_book_by_id,
    get_book_by_author,
    delete_book_by_author,
    get_or_create_author,
    get_all_authors,
)
from schemas import BookSchema, AuthorSchema

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
        schema = BookSchema()
        book = get_book_by_id(book_id)
        if book:
            return schema.dump(book), 200
        return f'Not found {book_id}', 404

    def put(self, book_id):
        schema = BookSchema()
        data = request.json
        logger.debug(data)
        try:
            new_book = schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        book = get_book_by_id(book_id)
        if book:
            new_book.id = book_id
            update_book_by_id(new_book)
            return schema.dump(new_book), 200
        return f'Not found {book_id}', 404

    def delete(self, book_id):
        delete_book_by_id(book_id)
        return '', 204


class AuthorsList(Resource):
    def get(self):
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True)

    def post(self):
        data = request.json
        schema = AuthorSchema()
        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        author = get_or_create_author(author.name, author.surname)
        return schema.dump(author), 201


api.add_resource(BookList, '/api/books')
api.add_resource(Book, '/api/books/<book_id>')
api.add_resource(AuthorsList, '/api/authors')


if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
