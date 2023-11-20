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
    return resultado, 200  


# LISTA TODOS OS CICLISTAS
@ciclista_app.route('/teste', methods=['GET'])
def listar_todos_ciclistas_route():
    try:
        # Lógica para obter a lista de ciclistas
        ciclistas = ciclista_service.listar_todos()
        return jsonify({"ciclistas": ciclistas})
    except Exception as e:
        # Se ocorrer uma exceção, trata como "Not Found"
        return jsonify({"error": "Not Found"}), 404