from flask import Blueprint, jsonify,request
from service.AluguelService import AluguelService

aluguel_app = Blueprint('aluguel_app', __name__)
aluguel_service = AluguelService()

@aluguel_app.route('/', methods=['POST'])
def alugar_bicicleta_route():
    data = request.json
    id_ciclista = data.get('id_ciclista')
    numero_tranca = data.get('trancaInicio')
    resultado_aluguel = aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
    return jsonify(resultado_aluguel)


@aluguel_app.route('/<int:id_bicicleta>/', methods=['GET'])
def listar_aluguel_route(id_bicicleta):
    resultado_aluguel = aluguel_service.obter_aluguel_por_bicicleta(id_bicicleta)
    return jsonify(resultado_aluguel)

@aluguel_app.route('/devolucao', methods=['POST'])
def devolver_bicicleta_route():
    data = request.json
    id_tranca = data.get('idTranca')
    id_bicicleta = data.get('idBicicleta')
    resultado_devolucao = aluguel_service.devolver_bicicleta(id_bicicleta, id_tranca)
    return jsonify(resultado_devolucao)



