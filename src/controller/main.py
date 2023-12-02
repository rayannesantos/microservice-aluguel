import os, sys
from flask import Flask,jsonify, request
from unittest.mock import Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
from service.CiclistaService import CiclistaService
from service.AluguelService import AluguelService
from service.FuncionarioService import FuncionarioService


from controller.CiclistaController import ciclista_app
from controller.AluguelController import aluguel_app
from controller.DevolucaoController import devolucao_app

app = Flask(__name__)

# ###### config do SONAR do problema de CSRF ###### 
# from flask_wtf import CSRFProtect               #
# from flask_wtf.csrf import generate_csrf        #
#                                                 #
# csrf = CSRFProtect(app)                         #
# csrf.init_app(app)                              #
# app.config['SECRET_KEY'] = 'teste123'           #
#                                                 #
# @app.route('/get_csrf_token', methods=['GET'])  #
# def get_csrf_token():                           #
#     token = generate_csrf()                     #
#     return token, 200                           #
# #################################################



@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World! :)"


# FUNCIONARIOS 

# @app.route('/funcionarios', methods=['GET'])
# def listar_funcionarios_route():
#     return listar_funcionarios()

# @app.route('/funcionarios/<int:id_funcionario>', methods=['GET'])
# def listar_funcionarios_id_route(id_funcionario):
#     return listar_funcionario_id(id_funcionario)


# @app.route('/funcionario', methods=['POST'])
# def cadastrar_funcionario_route():
#         data = request.json
#         senha = data.get("senha")
#         confirmacao_senha = data.get("confirmacao_senha")
#         email =  data.get("email")
#         nome = data.get("nome")
#         idade = data.get("idade")
#         funcao = data.get("funcao")
#         cpf = data.get("cpf")

#         response = cadastrar_funcionario(senha, confirmacao_senha, email, nome, idade, funcao, cpf)
#         return response


# @app.route('/funcionario/<int:id_funcionario>', methods=['PUT'])
# def editar_funcionario_route(id_funcionario):
#         data = request.json
#         senha = data.get("senha")
#         confirmacao_senha = data.get("confirmacao_senha")
#         email =  data.get("email")
#         nome = data.get("nome")
#         idade = data.get("idade")
#         funcao = data.get("funcao")
#         cpf = data.get("cpf")

#         response = editar_funcionario(id_funcionario, senha, confirmacao_senha, email, nome, idade, funcao,cpf)
#         return response
    

# @app.route('/funcionario/<int:id_funcionario>', methods=['DELETE'])
# def remover_funcionario_route(id_funcionario):
#         response = remover_funcionario(id_funcionario)
#         return response

# CICLISTA
@app.route('/ciclista/<int:id_ciclista>', methods=['GET'])
def listar_ciclista_id_route(id_ciclista):
    try:
        ciclista_service = CiclistaService()
        ciclista = ciclista_service.obter_ciclista_por_id_json(id_ciclista)
        return jsonify({"ciclista": ciclista})
    except Exception:
        return jsonify({"error": "Requisição mal formada"}), 404


@app.route('/ciclista/<int:id_ciclista>', methods=['PUT'])
def alterar_ciclista_id_route(id_ciclista):
    dados = request.json
    ciclista_service = CiclistaService()
    resultado = ciclista_service.alterar_ciclista(id_ciclista, dados)
    if "error" in resultado:
        return resultado, 422  

    return {"mensagem": "Dados atualizados", "ciclistas": resultado}, 200
    
    
@app.route('/ciclista/<int:id_ciclista>/permiteAluguel', methods=['GET'])
def permite_aluguel_route(id_ciclista):
        ciclista_service = CiclistaService()
        validacao = ciclista_service.permite_aluguel(id_ciclista)
        return jsonify(validacao)

@app.route('/ciclista/<int:id_ciclista>/bicicletaAlugada', methods=['GET'])
def bicicleta_alugada_route(id_ciclista):
        aluguel_service = AluguelService()
        bicicleta = aluguel_service.obter_bicicleta_alugada_por_ciclista(id_ciclista)
        return bicicleta


@app.route('/ciclista/existeEmail/<string:email>', methods=['GET'])
def existe_email_route(email):
        ciclista_service = CiclistaService()
        email = ciclista_service.verifica_email(email)
        return jsonify(email)


# TODO
# @app.route('/cartaoDeCredito/<int:id_ciclista>/', methods=['GET'])
# def listar_meio_de_pagamento_por_id(id_ciclista):
#     ciclista_service = CiclistaService()
#     meio_de_pagamento = ciclista_service.listar_meio_de_pagamento_por_id(id_ciclista)
    
#     if 'error' in meio_de_pagamento:
#         return jsonify({"error": "Não encontrado"}), 404
    
#     return jsonify(meio_de_pagamento)

# funcionarios

@app.route('/funcionario', methods=['GET'])
def listar_funcionarios_route():
    try:
        funcionario_service = FuncionarioService()
        funcionarios = funcionario_service.listar_todos_funcionarios()
        return jsonify({"funcionarios": funcionarios})
    except Exception:
        return jsonify({"error": "Requisição mal formada"}), 404

if __name__ == '__main__':
    # app.register_blueprint(ciclista_app, url_prefix='/ciclista')
    app.register_blueprint(aluguel_app, url_prefix='/aluguel')
    app.register_blueprint(devolucao_app, url_prefix='/devolucao')
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)