from flask import Blueprint, jsonify,request
from service.CiclistaService import CiclistaService

devolucao_app = Blueprint('devolucao_app', __name__)
devolucao_service = CiclistaService()

@devolucao_app.route('/', methods=['POST'])
def devolucao_bicicleta_route():
    data = request.json
    numero_tranca = data.get('idTranca')
    numero_bicicleta = data.get('idBicicleta')

    resultado_devolucao = devolucao_service.devolver_bicicleta(numero_tranca, numero_bicicleta)
    return jsonify(resultado_devolucao)

