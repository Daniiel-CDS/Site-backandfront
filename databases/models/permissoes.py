from peewee import CharField, Model
from databases.database import db

class permissoes(Model):
    nome_permissao = CharField(40,null=False)

    class Meta:
        database = db