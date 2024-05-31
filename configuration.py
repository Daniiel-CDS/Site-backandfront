from datetime import timedelta
from routes.home import home_route
from routes.clientes import clientes_route
from routes.encurtador import encurtador
from databases.database import db
from databases.models.cliente import Cliente
from databases.models.usuario import usuario
from databases.models.permissoes import permissoes
from databases.models.usuario_permissoes import usuario_permissoes
from databases.models.links import Link


#Configura tudo

def configure_all(app):
    configure_routes(app)
    configure_db()
    configure_app(app)

#Incia configuração das rotas
def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(clientes_route, url_prefix="/clientes")
    app.register_blueprint(encurtador, url_prefix="/enc")

def configure_app(app):
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
    app.config['SECRET_KEY'] = "secret"

#Configura o db e criar as tabelas do Banco de Dados;
def configure_db():
    db.connect()
    db.create_tables([Cliente,permissoes,usuario,usuario_permissoes,Link])