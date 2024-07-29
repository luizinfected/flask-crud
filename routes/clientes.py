from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


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
    return render_template('lista_clientes.html', clientes=CLIENTES)
    # return 'retornar todos clientes'


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # return 'inserir cliente no bd'
    data = request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email']
    }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new', methods=['GET'])
def form_cliente():
    return render_template('form_cliente.html')
    # return 'formulario para criar um cliente'
    

@cliente_route.route('/<int:cliente_id>', methods=['GET'])
def detalhe_cliente(cliente_id):
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)
    # return 'exibir detalhes do cliente'


@cliente_route.route('/<int:cliente_id>/edit', methods=['GET'])
def form_edit_cliente(cliente_id):
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_cliente.html', cliente=cliente)
    # return 'formulário para editar um cliente'


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    
    cliente_editado = None

    # obter dados do form de edicao
    data = request.json

    # obter usuario pelo id
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c

    # editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
    return 'deletar um cliente pelo id'    