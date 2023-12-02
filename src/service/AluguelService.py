from flask import jsonify
from service.CiclistaService import CiclistaService
from datetime import datetime
from model.AluguelModel import AluguelBicicleta
import requests

class AluguelService:
    DISPONIVEL = "Disponível"
    INDISPONIVEL = "Indisponível"
    OCUPADA = "Ocupada"
    
    def __init__(self):
        self.bicicletas = [
            {
                "id": 1,
                "marca": "Caloi",
                "modelo": "Mountain Bike",
                "ano": "2022",
                "numero": 101,
                "status": self.DISPONIVEL
            },
            {
                "id": 2,
                "marca": "Specialized",
                "modelo": "Road Bike",
                "ano": "2021",
                "numero": 102,
                "status": self.INDISPONIVEL
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
                "status": self.DISPONIVEL
            }
        ]
        
        self.alugueis = [
            {
                "bicicleta": 1,
                "ciclista":3,
                "trancaInicio": 50
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

        if ciclista.status_aluguel == True:
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
            
            
            
            self.alterar_status_bicicleta(numero_bicicleta, self.DISPONIVEL)

            self.alterar_status_tranca(numero_tranca, self.OCUPADA)            

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

    def obter_bicicleta_alugada_por_ciclista(self, id_ciclista):
        ciclista_service = CiclistaService()
        ciclista = ciclista_service.obter_ciclista_por_id(id_ciclista)
        
        if ciclista is None:
            return jsonify({'error': 'Ciclista não encontrado'}), 404

        for aluguel in self.alugueis:
            if aluguel['ciclista'] == ciclista:  # Correção aqui
                # chamando microservice-equipamento
                id_bicicleta = ciclista['bicicleta']
                url_bicicleta = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/bicicleta/{id_bicicleta}'
                response = requests.get(url_bicicleta)
                
                if response.status_code == 200:
                    data = response.json()
                    return jsonify(data)
                else:
                    return jsonify({'error': 'Erro ao chamar a API'}), 500

        return jsonify({}), 404

    
    

    def obter_aluguel_por_bicicleta(self, numero_bicicleta):
        for aluguel in self.alugueis: 
            if aluguel.bicicleta == numero_bicicleta:
                return aluguel.to_dict()  
        return None
    
    
    # def chamar_microservice_equipamento():
    #     url = 'https://bike-rent-g5cdxjx55q-uc.a.run.app/'
    #     # Fazendo a requisição GET para a API
    #     response = requests.get(url)
    #     # Verificando se a requisição foi bem-sucedida (código 200)
    #     if response.status_code == 200:
    #         # Convertendo a resposta JSON para um dicionário Python
    #         data = response.json()
    #         return jsonify(data)
    #     else:
    #         # Em caso de erro, retornar uma mensagem apropriada
    #         return jsonify({'error': 'Erro ao chamar a API'}), 500