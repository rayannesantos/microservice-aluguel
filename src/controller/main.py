import os, sys
from flask import Flask
from flask import Flask, request
from unittest.mock import Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.CiclistaService import cadastrar_ciclista, listar_ciclistas,ativar_ciclista
from service.FuncionarioService import listar_funcionarios, cadastrar_funcionario, editar_funcionario, remover_funcionario, listar_funcionario_id

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World! :)"


# CICLISTAS
@app.route('/ciclista', methods=['POST'])
def cadastrar_ciclista_route():
        data = request.json
        return cadastrar_ciclista(data)


@app.route('/ciclista/<int:id_ciclista>/ativar', methods=['POST'])
def ativar_ciclista_route(id_ciclista):
    return ativar_ciclista(id_ciclista)


@app.route('/ciclistas', methods=['GET'])
def listar_ciclistas_route():
    return listar_ciclistas()


# FUNCIONARIOS 

@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios_route():
    return listar_funcionarios()

@app.route('/funcionarios/<int:id_funcionario>', methods=['GET'])
def listar_funcionarios_id_route(id_funcionario):
    return listar_funcionario_id(id_funcionario)


@app.route('/funcionario', methods=['POST'])
def cadastrar_funcionario_route():
        data = request.json
        senha = data.get("senha")
        confirmacao_senha = data.get("confirmacao_senha")
        email =  data.get("email")
        nome = data.get("nome")
        idade = data.get("idade")
        funcao = data.get("funcao")
        cpf = data.get("cpf")

        response = cadastrar_funcionario(senha,confirmacao_senha,email, nome, idade, funcao, cpf)
        return response


@app.route('/funcionario/<int:id_funcionario>', methods=['PUT'])
def editar_funcionario_route(id_funcionario):
        data = request.json
        senha = data.get("senha")
        confirmacao_senha = data.get("confirmacao_senha")
        email =  data.get("email")
        nome = data.get("nome")
        idade = data.get("idade")
        funcao = data.get("funcao")
        cpf = data.get("cpf")

        response = editar_funcionario(id_funcionario,senha,confirmacao_senha,email, nome, idade,funcao,cpf)
        return response
    

@app.route('/funcionario/<int:id_funcionario>', methods=['DELETE'])
def remover_funcionario_route(id_funcionario):
        response = remover_funcionario(id_funcionario)
        return response
    

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)