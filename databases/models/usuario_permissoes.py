from peewee import CharField, Model,ForeignKeyField
import datetime
from databases.database import db
from databases.models.usuario import usuario
from databases.models.permissoes import permissoes 

class usuario_permissoes(Model):
    usuario =  ForeignKeyField(usuario, backref='permissoes')
    permissao = ForeignKeyField(permissoes, backref='usuario')


    class Meta:
        database = db