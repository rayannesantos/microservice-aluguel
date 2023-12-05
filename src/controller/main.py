import os, sys
from flask import Flask,jsonify, request
from unittest.mock import Mock
import requests

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
from service.CiclistaService import CiclistaService
from service.AluguelService import AluguelService
from service.FuncionarioService import FuncionarioService

funcionario_service = FuncionarioService()



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

# CICLISTA
ciclista_service = CiclistaService()

@app.route('/ciclista', methods=['POST'])
def cadastrar_ciclista():
        dados = request.json
        ciclista = ciclista_service.cadastrar_ciclista(dados)
        return ciclista


@app.route('/ciclista/<int:id_ciclista>', methods=['GET'])
def listar_ciclista_id_route(id_ciclista):
    try:
        ciclista = ciclista_service.obter_ciclista_por_id_json(id_ciclista)
        return jsonify({"ciclista": ciclista})
    except Exception:
        return jsonify({"error": "Requisição mal formada"}), 404


@app.route('/ciclista/<int:id_ciclista>', methods=['PUT'])
def alterar_ciclista_id_route(id_ciclista):
    dados = request.json
    resultado = ciclista_service.alterar_ciclista(id_ciclista, dados)
    if "error" in resultado:
        return resultado, 422  

    return {"mensagem": "Dados atualizados", "ciclistas": resultado}, 200
    
    
@app.route('/ciclista/<int:id_ciclista>/permiteAluguel', methods=['GET'])
def permite_aluguel_route(id_ciclista):
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


@app.route('/ciclista/<int:id_ciclista>/ativar', methods=['GET'])
def ativar_ciclista(id_ciclista):
    ativar = ciclista_service.ativar_ciclista(id_ciclista)
    return jsonify(ativar)


@app.route('/cartaoDeCredito/<int:id_ciclista>/', methods=['GET'])
def listar_meio_de_pagamento_por_id(id_ciclista):
    meio_de_pagamento = ciclista_service.listar_meio_de_pagamento_por_id(id_ciclista)
    if 'error' in meio_de_pagamento:
        return jsonify({"error": "Não encontrado"}), 404
    
    return jsonify(meio_de_pagamento)

@app.route('/cartaoDeCredito/<int:id_ciclista>/', methods=['PUT'])
def alterar_meio_de_pagamento_por_id(id_ciclista):
    dados = request.json
    meio_de_pagamento = ciclista_service.alterar_meio_de_pagamento(id_ciclista,dados)
    if 'error' in meio_de_pagamento:
        return jsonify({"error": "Não alterado"}), 404
    
    return jsonify(meio_de_pagamento)

@app.route('/allciclistas', methods=['GET'])
def listar_tpdos_os_ciclistas_route():
        ciclistas = ciclista_service.listar_todos()
        return jsonify({"ciclistas": ciclistas})



@app.route('/funcionario', methods=['POST'])
def cadastrar_funcionario():
        dados = request.json
        funcionario = funcionario_service.cadastrar_funcionario(dados)
        return funcionario
    
@app.route('/funcionario/<int:id_funcionario>/', methods=['PUT'])
def alterar_funcionario(id_funcionario):
    dados = request.json
    funcionario = funcionario_service.alterar_funcionario(id_funcionario,dados)
    if 'mensagem' in funcionario:
        return jsonify(funcionario)
    else:
        return jsonify({"error": "Funcionário não alterado"}), 404

@app.route('/funcionario', methods=['GET'])
def listar_funcionarios_route():
    try:
        funcionarios = funcionario_service.listar_todos_funcionarios()
        return jsonify({"funcionarios": funcionarios})
    except Exception:
        return jsonify({"error": "Requisição mal formada"}), 404

@app.route('/funcionario/<int:id_funcionario>', methods=['GET'])
def listar_funcionario_id_route(id_funcionario):
    try:
        funcionario = funcionario_service.obter_funcionario_por_id_json(id_funcionario)
        
        if funcionario:
            return jsonify(funcionario)
        else:
            return jsonify({"error": "Não encontrado"}), 404
    except Exception:
        return jsonify({"error": "Erro interno"}), 500

@app.route('/funcionario/<int:id_funcionario>', methods=['DELETE'])
def deletar_funcionario_id_route(id_funcionario):
        if funcionario_service.remover_funcionario_por_id(id_funcionario):
            return jsonify({'message': 'Funcionário removido com sucesso'}), 200
        else:
            return jsonify({'error': 'Funcionário não encontrado'}), 404

            


from service.AluguelService import AluguelService
aluguel_service = AluguelService()

@app.route('/aluguel', methods=['POST'])
def alugar_bicicleta_route():
    data = request.json
    id_ciclista = data.get('id_ciclista')
    numero_tranca = data.get('tranca_inicio')
    resultado_aluguel = aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
    return jsonify(resultado_aluguel)


@app.route('/devolucao', methods=['POST'])
def devolvet_bicicleta_route():
    data = request.json
    id_bicicleta = data.get('id_bicicleta')
    id_tranca = data.get('id_tranca')
    resultado_devolucao = aluguel_service.devolver_bicicleta(id_bicicleta, id_tranca)
    print (resultado_devolucao)
    return jsonify(resultado_devolucao)


def enviar_email(assunto, mensagem):
    url = "https://microservice-externo-b4i7jmshsa-uc.a.run.app/enviarEmail"

    data = {
        "destinatario": "bqueiroz@edu.unirio.br",
        "assunto": assunto,
        "mensagem": mensagem
    }
    response = requests.post(url, json=data)
    print(response.text)
    if response.status_code != 200:
        return False
    
    return True

def obter_tranca(numero_tranca):
    url_tranca = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/tranca/{numero_tranca}'
    response = requests.get(url_tranca)  
    return response

def obter_bicicleta(numero_bicicleta):
    url_bicicleta = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/bicicleta/{numero_bicicleta}'
    response = requests.get(url_bicicleta)  
    return response

def chamar_cobranca(id_ciclista):
        dados_cobranca = {"valor": 10, "ciclista": str(id_ciclista)}
        url_cobranca = 'https://microservice-externo-b4i7jmshsa-uc.a.run.app/cobranca'
        response = requests.post(url_cobranca, json = dados_cobranca)
        if response.status_code == 200:
            return True
        return False
            
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
