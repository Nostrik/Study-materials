from peewee import Model, SqliteDatabase, DateTimeField, IntegerField, CharField, TextField, ForeignKeyField


db = SqliteDatabase('database.db')


class BaseModel(Model):

    class Meta:
        database = db


class User_Data(BaseModel):
    date = DateTimeField(null=True)
    telegram_id = IntegerField(null=True)
    user_name = CharField(null=True)
    command = TextField(null=True)


class Hotel_Data(BaseModel):
    user = ForeignKeyField(User_Data, related_name='hotel')
    name = CharField(null=True)
    city = CharField(null=True)
    address = TextField(null=True)
    price = CharField(null=True)
