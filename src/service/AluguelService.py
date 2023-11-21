from service.CiclistaService import CiclistaService
from datetime import datetime
from model.AluguelModel import AluguelBicicleta

class AluguelService:
    def __init__(self):
        # Inicializa dados de bicicletas e trancas mockados
        self.bicicletas = [
            {
                "id": 1,
                "marca": "Caloi",
                "modelo": "Mountain Bike",
                "ano": "2022",
                "numero": 101,
                "status": "Disponível"
            },
            {
                "id": 2,
                "marca": "Specialized",
                "modelo": "Road Bike",
                "ano": "2021",
                "numero": 102,
                "status": "Indisponível"
            }
        ]

        self.trancas = [
            {
                "id": 50,
                "bicicleta": 1,
                "numero": 100,
                "localizacao": "Estação A",
                "anoDeFabricacao": "2022",
                "modelo": "Tranca A",
                "status": "Disponível"
            }
        ]

    # UC03 – Alugar bicicleta 
    def alugar_bicicleta(self, id_ciclista, numero_tranca):
        # Validando dados para alugar bicicleta
        trancadesejada = None
        for tranca in self.trancas:
            if tranca["numero"] == numero_tranca:
                trancadesejada = tranca
                break

        if trancadesejada is None:
            return {"error": "Tranca não encontrada"}, 404

        ciclista_service = CiclistaService()
        ciclista = ciclista_service.obter_ciclista_por_id(id_ciclista)

        if ciclista is None:
            return {"error": "Ciclista não encontrado"}, 404

        if ciclista.status_aluguel:
            return {"error": "Ciclista já tem um aluguel"}, 422


        aluguel = AluguelBicicleta(
            bicicleta=trancadesejada["bicicleta"],
            hora_inicio=datetime.now(),
            tranca_inicio=numero_tranca,
            ciclista=ciclista.nome
        )


        return {"success": "Aluguel realizado", "registro_retirada": aluguel.to_dict()}, 200
