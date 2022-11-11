from typing import Dict

from marshmallow import Schema, fields, validates, ValidationError, post_load

from models import get_book_by_title, Book, get_book_by_author, get_book_by_id


class BookSchema(Schema):

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)

    @validates('title')
    def validate_title(self, title: str) -> None:
        if get_book_by_title(title) is not None:
            raise ValidationError(
                'Book with title "{title}" already exists, '
                'please use a different title.'.format(title=title)
            )

    @validates('author')
    def validate_author(self, author: str) -> None:
        if get_book_by_author(author) is not None:
            raise ValidationError(
                'Book with title "{author}" already exists, '
                'please use a different title.'.format(author=author)
            )

    @validates('id')
    def validate_id(self, book_id: str) -> None:
        if get_book_by_id(int(book_id)) is not None:
            raise ValidationError(
                'Book with id "{id}" already exists, '
                'please use a different id.'.format(id=book_id)
            )

    @post_load
    def create_book(self, data: Dict, **kwargs) -> Book:
        return Book(**data)
