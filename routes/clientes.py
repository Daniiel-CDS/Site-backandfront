from flask import Blueprint, render_template, request
from databases.models.cliente import Cliente
import bcrypt

clientes_route = Blueprint("clientes", __name__)
"""
/clientes/ - (GET) - Listar cliente
/clientes/ - (POST) - Adicionar um cliente
/clientes/new - (GET) - Formulario para criação de um cliente
/clientes/<id> - (GET) - Obter dados de um cliente
/clientes/<id>/edit -(GET) - Renderizar um formulario para editar um cliente
/clientes/<id>/update - (PUT) - Atualizar os dados de um cliente
/clientes/<id>/delete - (DELETE) - deleta o registro do usuário
"""
@clientes_route.route('/')
def lista_cliente():
    """ Listar os clientes"""
    clientes = Cliente.select()
    return render_template("lista_clientes.html",clients=clientes)

@clientes_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir dados cliente"""
    data = request.json
    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )

    clients.append(novo_usuario)
    cliente = novo_usuario
    return render_template("item_cliente.html", cliente=cliente )

@clientes_route.route('/new', methods=['GET'])
def form_cliente():
    """Exibir formulario para adicionar novo cliente"""
    return render_template("form_cliente.html")


@clientes_route.route('/<int:client_id>')
def detalhe_cliente(client_id):
    """EXIBIR DADOS DE UM CLIENTE"""
    return render_template("detalhe_cliente.html")
    
@clientes_route.route('/<int:client_id>/edit')
def form_edit_cliente(client_id):
    """Formulário para editar um cliente"""
    cliente = None
    cliente = Cliente.get_by_id(client_id)
    return render_template("form_edit_cliente.html", cliente=cliente)

@clientes_route.route('/<int:client_id>/update', methods=['PUT'])
def update_cliente(client_id):
    #Obter dados do usuário pelo formulario
    data = request.json
    #obter usuário pelo ID
    pessoa = Cliente.get_by_id(client_id)
    pessoa.nome = data['nome']
    pessoa.email = data['email']
    pessoa.save()

    return render_template('item_cliente.html', cliente=pessoa)


@clientes_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_cliente(client_id):
    """Deletar Cliente"""
    cliente = Cliente.get_by_id(client_id)
    cliente.delete_instance()

    return {'delete':'ok'}


@clientes_route.route('/<int:client_id>/delete', methods=['POST'])
def subir_imagem():
    return '' 