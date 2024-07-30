from peewee import *

db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db

