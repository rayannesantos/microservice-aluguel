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
        
        self.alugueis = []

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
        
        self.alugueis.append(aluguel)


        return {"success": "Aluguel realizado", "registro_retirada": aluguel.to_dict()}, 200


    def devolver_bicicleta(self, numero_bicicleta, numero_tranca):
            # Encontra o aluguel correspondente à bicicleta devolvida
            aluguel_correspondente = None
            for aluguel in self.alugueis:
                if aluguel.bicicleta == numero_bicicleta:
                    aluguel_correspondente = aluguel
                    break     
                       
            if aluguel_correspondente is None:
                return {"error": "Aluguel não encontrado para a bicicleta especificada"}, 404
            else:
                aluguel_correspondente.hora_fim = datetime.now()
                aluguel_correspondente.tranca_fim = numero_tranca
            
            
            
            self.alterar_status_bicicleta(numero_bicicleta, "Disponível")

            self.alterar_status_tranca(numero_tranca, "Ocupada")            

            return {"success": "Bicicleta devolvida com sucesso", "registro_devolucao": aluguel_correspondente.to_dict()}, 200



    def calcular_valor_a_pagar(self, horas_excedidas):
        return 5.0 * horas_excedidas

    def enviar_email(self):
        return True


    def alterar_status_bicicleta(self, numero_bicicleta, novo_status):
        for bicicleta in self.bicicletas:
            if bicicleta["numero"] == numero_bicicleta:
                bicicleta["status"] = novo_status
                break
            

    def alterar_status_tranca(self, numero_tranca, novo_status):
        for tranca in self.trancas:
            if tranca["numero"] == numero_tranca:
                tranca["status"] = novo_status
                break


    def obter_aluguel_por_bicicleta(self, numero_bicicleta):
        for aluguel in self.alugueis: 
            if aluguel.bicicleta == numero_bicicleta:
                return aluguel.to_dict()  # Utiliza o método to_dict para obter um dicionário
        return None