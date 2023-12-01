import os, sys
from flask import Flask,request
from unittest.mock import Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


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

        response = cadastrar_funcionario(senha, confirmacao_senha, email, nome, idade, funcao, cpf)
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

        response = editar_funcionario(id_funcionario, senha, confirmacao_senha, email, nome, idade, funcao,cpf)
        return response
    

@app.route('/funcionario/<int:id_funcionario>', methods=['DELETE'])
def remover_funcionario_route(id_funcionario):
        response = remover_funcionario(id_funcionario)
        return response
    

if __name__ == '__main__':
    app.register_blueprint(ciclista_app, url_prefix='/ciclista')
    app.register_blueprint(aluguel_app, url_prefix='/aluguel')
    app.register_blueprint(devolucao_app, url_prefix='/devolucao')
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)