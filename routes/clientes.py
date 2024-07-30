from flask import Blueprint, render_template, request
from database.database import db, Usuario

db.connect()

db.create_tables([Usuario])

# usuario = Usuario.create(nome="Luiz Costa", email='luiz@gmail.com')
# usuario3 = Usuario.create(nome="Maik Carvalho", email='maik@gmail.com')
# usuario4 = Usuario.create(nome="Vinicius", email='vinicius@gmail.com')

cliente_route = Blueprint('cliente', __name__)

# Rota de clientes
#   - /clientes/ (GET) - listar os clientes
#   - /clientes/ (POST) - inserir o cliente no servidor
#   - /clientes/new (GET) - renderizar o formulário para criar o cliente
#   - /clientes/<id> (GET) - obter os dados de um cliente
#   - /clientes/<id>/edit (GET) - renderizar um formulario para editar o cliente
#   - /clientes/<id>/update (PUT) - atualizar os dados do cliente
#   - /clientes/<id>/delete (DELETE) - delete o registro do usuário


@cliente_route.route('/')
def lista_clientes():
    lista_usuarios = Usuario.select()
    return render_template('lista_clientes.html', clientes=lista_usuarios)



@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json
    novo_usuario = Usuario.create(nome=data["nome"], email=data["email"])
    return render_template('item_cliente.html', cliente=novo_usuario)



@cliente_route.route('/new', methods=['GET'])
def form_cliente():
    return render_template('form_cliente.html')



@cliente_route.route('/<int:cliente_id>', methods=['GET'])
def detalhe_cliente(cliente_id):
    cliente = Usuario.get(Usuario.id == cliente_id)
    print(cliente)
    return render_template('detalhe_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/edit', methods=['GET'])
def form_edit_cliente(cliente_id):
    cliente = Usuario.get(Usuario.id == cliente_id)
    return render_template('form_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):

    cliente = Usuario.get(Usuario.id == cliente_id)

    data = request.json
  
    cliente.nome = data['nome']
    cliente.email = data['email']

    cliente.save()
    return render_template('item_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    Usuario.delete_by_id(cliente_id)
