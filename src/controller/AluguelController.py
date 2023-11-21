from flask import Blueprint, jsonify,request
# from service.CiclistaService import CiclistaService
from service.AluguelService import AluguelService

aluguel_app = Blueprint('aluguel_app', __name__)
aluguel_service = AluguelService()

@aluguel_app.route('/', methods=['POST'])
def alugar_bicicleta_route():
    data = request.json
    # Certifique-se de que 'id_ciclista', 'numero_tranca' e 'bicicleta_tranca' estão presentes nos dados
    id_ciclista = data.get('id_ciclista')
    numero_tranca = data.get('trancaInicio')
    resultado_aluguel = aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
    return jsonify(resultado_aluguel)
