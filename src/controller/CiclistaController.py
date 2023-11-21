# a camada de Controllers faz o "primeiro contato" com as requisições, enviando a camada de Services 
# apenas as informações relevantes para completar a requisição. Além disso, essa é a camada que irá enviar
# a resposta ao cliente, seja ela positiva ou negativa.
###########################################################################################################
# Realizar apenas operações relacionadas a Request e Response (HTTP)
# Não possuir "conhecimento" sobre regras de negócios, ou acesso ao DB
# Formada quase que exclusivamente por Middlewares


from flask import Blueprint, jsonify,request
from service.CiclistaService import CiclistaService

ciclista_app = Blueprint('ciclista_app', __name__)
ciclista_service = CiclistaService()



# ALTERAR CICLISTA
@ciclista_app.route('/<int:id_ciclista>', methods=['PUT'])
def alterar_ciclista_id_route(id_ciclista):
    dados = request.json
    resultado = ciclista_service.alterar_ciclista(id_ciclista, dados)
    
    if "error" in resultado:
        return resultado, 422  

    return {"mensagem": "Dados atualizados", "ciclistas": resultado}, 200



@ciclista_app.route('<int:id_ciclista>/CartaoDeCredito', methods=['PUT'])
def alterar_cartao_route(id_ciclista):
    dados_cartao = request.json.get('dados_cartao', {})
    resultado = ciclista_service.alterar_cartao(id_ciclista, dados_cartao)
    return jsonify(resultado)

# LISTA TODOS OS CICLISTAS
@ciclista_app.route('/teste', methods=['GET'])
def listar_todos_ciclistas_route():
    try:
        # Lógica para obter a lista de ciclistas
        ciclistas = ciclista_service.listar_todos()
        return jsonify({"ciclistas": ciclistas})
    except Exception:
        # Se ocorrer uma exceção, trata como "Not Found"
        return jsonify({"error": "Not Found"}), 404
    
    
# LISTA meio de pagamento
@ciclista_app.route('/<int:id_ciclista>/pagamento', methods=['GET'])
def listar_meio_de_pagamento_por_id(id_ciclista):
    meio_de_pagamento = ciclista_service.listar_meio_de_pagamento_por_id(id_ciclista)
    
    if 'error' in meio_de_pagamento:
        return jsonify({"error": "Ciclista or meio de pagamento not found"}), 404
    
    return jsonify(meio_de_pagamento)

