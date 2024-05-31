from peewee import Model, CharField
from databases.database import db


class Link(Model):
    link = CharField()


    class Meta():
        database = db
