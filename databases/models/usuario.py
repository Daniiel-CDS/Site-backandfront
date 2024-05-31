from peewee import CharField, Model, DateTimeField, IntegerField,BlobField
import datetime
from databases.database import db

class usuario(Model):
    nome = CharField(30)
    senha = CharField(255)
    idade = IntegerField(null=False)
    email = CharField(unique=True)
    data_criacao = DateTimeField(default=datetime.datetime.now)
    imagem = BlobField(null=True)

    class Meta:
        database = db