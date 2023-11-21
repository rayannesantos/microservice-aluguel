from flask import Blueprint, jsonify, request
from service.AluguelService import AluguelService

devolucao_app = Blueprint('devolucao_app', __name__)
devolucao_service = AluguelService()

@devolucao_app.route('/', methods=['POST'])
def devolver_bicicleta_route():
    data = request.json
    id_tranca = data.get('idTranca')
    id_bicicleta = data.get('idBicicleta')
    resultado_devolucao = devolucao_service.devolver_bicicleta(id_bicicleta, id_tranca)
    return jsonify(resultado_devolucao)
