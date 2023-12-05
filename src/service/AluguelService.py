from flask import jsonify
from service.CiclistaService import CiclistaService
from datetime import datetime, timedelta
from model.AluguelModel import AluguelBicicleta
import requests


hora_atual = datetime.now()

class AluguelService:
    TRANCA_INICIAL = "Tranca inicial"
    COBRANCA_INICIAL = "Cobranca inicial"
    DATA_INICIO = "Data início"

    
    
    def __init__(self):
        self.alugueis = [
            {
                "ciclista": 3,
                "Bicicleta": 3,
                self.TRANCA_INICIAL: 2,
                "Status": "EM_ANDAMENTO",
                self.COBRANCA_INICIAL: 1,
                self.DATA_INICIO: hora_atual.strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "ciclista": 4,
                "Bicicleta": 5,
                self.TRANCA_INICIAL: 4,
                "Status": "EM_ANDAMENTO",
                self.COBRANCA_INICIAL: 2,
                self.DATA_INICIO: (hora_atual - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "ciclista": 3,
                "Bicicleta": 1,
                self.TRANCA_INICIAL: 1,
                "Tranca final": 2,
                "Status": "FINALIZADO COM COBRANCA EXTRA PENDENTE",
                self.COBRANCA_INICIAL: 3,
                "Data início": (hora_atual - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
                self.DATA_INICIO: hora_atual.strftime("%Y-%m-%d %H:%M:%S")
            }
        ]
        
    def alugar_bicicleta(self, id_ciclista, numero_tranca): 
        url_tranca = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/tranca/{numero_tranca}'
        response = requests.get(url_tranca)  

        if response.status_code == 404:
            return {"error": "Tranca não encontrada"}, 404 
        
        if response.status_code == 200:        
            ciclista_service = CiclistaService()
            ciclista = ciclista_service.obter_ciclista_por_id(id_ciclista)

            if ciclista is None:
                return {"error": "Ciclista não encontrado"}, 404

            if ciclista.status_aluguel:
                return {"error": "Ciclista já tem um aluguel"}, 422

            # Chamar cobrança
            dados_cobranca = {"valor": 10, "ciclista": str(id_ciclista)}
            valida_cobranca = self.chamar_cobranca(dados_cobranca)

            if not valida_cobranca:
                return {"error": "Falha na cobrança"}, 422

            hora_atual = datetime.now()
            
            dados_json = response.json()

            bicicleta = dados_json.get("bicicleta")            
            
            aluguel = AluguelBicicleta(
                bicicleta=bicicleta,
                hora_inicio=hora_atual.strftime("%Y-%m-%d %H:%M:%S"),
                tranca_inicio=numero_tranca,
                ciclista=ciclista  
            )
            
                    
            url_status_tranca = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/tranca/{numero_tranca}/status/6'
            response_tranca = requests.post(url_status_tranca)
            
            url_status_bicicleta = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/bicicleta/{bicicleta}/status/2'
            response_bicicleta = requests.post(url_status_bicicleta)

            try:
                ciclista_service.requisita_enviar_email("Dados do aluguel", aluguel.to_dict())
                self.alugueis.append(aluguel)
                print(aluguel)
                return {"success": "Aluguel realizado", "registro_retirada": aluguel.to_dict()}, 200
            except Exception as e:
                return {"error": f"Erro ao processar aluguel: {str(e)}"}, 500
        
        
    def chamar_cobranca(self, dados): 
        url_cobranca = 'https://microservice-externo-b4i7jmshsa-uc.a.run.app/cobranca'
        response = requests.post(url_cobranca, json = dados)
        if response.status_code == 200:
            return True
        return False

    def devolver_bicicleta(self, numero_bicicleta, numero_tranca):
        aluguel_correspondente = None
    
        for aluguel in self.alugueis:
            if aluguel['Bicicleta'] == numero_bicicleta:  
                aluguel_correspondente = aluguel
                print(aluguel_correspondente)
                        
        if aluguel_correspondente is None:
            return {"error": "Aluguel não encontrado para a bicicleta especificada"}, 404

        aluguel_correspondente['Data fim'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        aluguel_correspondente['Tranca final'] = numero_tranca
        
        url_status_tranca = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/tranca/{numero_tranca}/status/3'
        response_tranca = requests.post(url_status_tranca)

        url_status_bicicleta = f'https://bike-rent-g5cdxjx55q-uc.a.run.app/bicicleta/{numero_bicicleta}/status/1'
        response_bicicleta = requests.post(url_status_bicicleta)

        if response_tranca.status_code == 200 and response_bicicleta.status_code == 200:            
            return {"success": "Bicicleta devolvida com sucesso", "registro_devolucao": aluguel_correspondente}, 200


        return {"Mensagem": "Erro ao devolver bicicleta"}, 422



    def calcular_valor_a_pagar(self, horas_excedidas):
        return 5.0 * horas_excedidas

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
            if aluguel['ciclista'] == ciclista:  
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
    
    
