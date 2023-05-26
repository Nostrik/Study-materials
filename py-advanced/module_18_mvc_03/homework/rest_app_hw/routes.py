import logging
from typing import Tuple, List, Dict
from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flasgger import APISpec, Swagger

from werkzeug.serving import WSGIRequestHandler

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

spec = APISpec(
    title='Books and Authors',
    version='1.0.0',
    openapi_version='2.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)


class BookList(Resource):
    def get(self) -> Tuple[List[Dict], int]:
        """
        This is an endpoint for obtaining the books list.
        ---
        tags:
          - books
        responses:
          200:
            description: Books data
            schema:
              type: array
              items:
                $ref: '#/definitions/Book'
        """
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> Tuple[Dict, int]:
        """
        This is an endpoint for book creation.
        ---
        tags:
         - books
        parameters:
         - in: body
           name: new book params
           schema:
             $ref: '#/definitions/Book'
        responses:
         201:
           description: The book has been created
           schema:
             $ref: '#/definitions/Book'
        """

        data = request.json

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201


class Book(Resource):
    def get(self, book_id: int):
        """
        This is the endpoint for getting the book by id.
        ---
        tags:
          - book
        parameters:
          - in: url
            name: book id
            schema:
                $ref: '#/definitions/Book'
        responses:
          200:
            description: Book data
            schema:
              type: array
              items:
                $ref: '#/definitions/Book'
        """
        schema = BookSchema()
        book = get_book_by_id(book_id)
        if book:
            return schema.dump(book), 200
        return f'Not found {book_id}', 404

    def put(self, book_id):
        """
        This is an endpoint for updating Book.
        ---
        tags:
          - book
        parameters:
          - in: url
            name: book id
            schema:
              $ref: '#/definitions/Book'
        responses:
          200:
            description: The book has been updated.
            schema:
              $ref: '#/definitions/Book'
          404:
            description: Not found book id
          400:
            description: Validation error
        """
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
        """
        This is an endpoint for delete book by id.
        ---
        tags:
          - book
        parameters:
          - in: url
            name: book id
            schema:
              $ref: '#/definitions/Book'
        """
        delete_book_by_id(book_id)
        return '', 204


class AuthorsList(Resource):
    def get(self):
        """
        This is an endpoint for obtaining the author list.
        ---
        tags:
          - author
        responses:
          200:
            description: Authors data
            schema:
              $ref: '#/definitions/Author'
        """
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True)

    def post(self):
        """
        This is an endpoint for author creation.
        ---
        tags:
         - author
        parameters:
          - in: body
            name: new author params
            schema:
              $ref: '#/definitions/Author'
        responses:
          201:
            description: The new author has been created
            schema:
              $ref: '#/definitions/Author'
          400:
            description: Validation error
        """
        data = request.json
        schema = AuthorSchema()
        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        author = get_or_create_author(author.name, author.surname)
        return schema.dump(author), 201


template = spec.to_flasgger(
    app,
    definitions=[BookSchema, AuthorSchema]
)

swagger = Swagger(app, template=template)

api.add_resource(BookList, '/api/books')
api.add_resource(Book, '/api/books/<book_id>')
api.add_resource(AuthorsList, '/api/authors')


if __name__ == '__main__':
    init_db(initial_records=DATA)
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True)
