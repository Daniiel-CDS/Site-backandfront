from peewee import CharField, Model, DateTimeField
import datetime
from databases.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_criado = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db