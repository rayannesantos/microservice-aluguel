# UC01–Cadastrar Ciclista
from unittest.mock import Mock
from model.CiclistaModel import Ciclista
from model.MeiodePagamentoModel import MeioDePagamento  
import re
import requests
from flask import jsonify, Response
import string
import random

class CiclistaService: 
    def __init__(self):
        self.ciclistas_data = [
            {
                "id_ciclista": 1,
                "nome": "Fulano Beltrano",
                "nascimento": "2021-05-02",
                "cpf": "78804034009",
                "passaporte": {
                    "numero": "4012001037141112",
                    "validade": "2022-12",
                    "pais": "BR"
                },
                "nacionalidade": "Brasileiro",
                "email": "user@example.com",
                "url_foto_documento": "string",
                "senha": "ABC123"
            },
            {
                "id_ciclista": 2,
                "nome": "Fulano Beltrano",
                "nascimento": "2021-05-02",
                "cpf": "43943488039",
                "passaporte": {
                    "numero": "4012001037141112",
                    "validade": "2022-12",
                    "pais": "BR"
                },
                "nacionalidade": "Brasileiro",
                "email": "user2@example.com",
                "senha": "ABC123"
            },
            {
                "id_ciclista": 3,
                "nome": "Fulano Beltrano",
                "nascimento": "2021-05-02",
                "cpf": "10243164084",
                "nacionalidade": "Brasileiro",
                "email": "user3@example.com",
                "senha": "ABC123"
            },
            {
                "id_ciclista": 4,
                "nome": "Fulano Beltrano",
                "nascimento": "2021-05-02",
                "cpf": "30880150017",
                "nacionalidade": "Brasileiro",
                "email": "user4@example.com",
                "senha": "ABC123"
            }
        ]
        self.ciclistas = [Ciclista(**data) for data in self.ciclistas_data]
        
    meio_de_pagamento_data = [
        {
            "nome_titular": "Fulano Beltrano",
            "numero": "4012001037141112",
            "validade": "2022-12",
            "cvv": "132",
            "ciclista": 1
        },
        {
            "nome_titular": "Fulano Beltrano",
            "numero": "4012001037141112",
            "validade": "2022-12",
            "cvv": "132",
            "ciclista": 2
        },
        {
            "nome_titular": "Fulano Beltrano",
            "numero": "4012001037141112",
            "validade": "2022-12",
            "cvv": "132",
            "ciclista": 3
        },
        {
            "nome_titular": "Fulano Beltrano",
            "numero": "4012001037141112",
            "validade": "2022-12",
            "cvv": "132",
            "ciclista": 4
        }
]
    def cadastrar_ciclista(self, request_data):
        email = request_data.get('ciclista', {}).get('email')
        if email and re.match(r'^\S+@\S+\.\S+$', email):
            # Verificar nacionalidade
            nacionalidade = request_data.get('ciclista', {}).get('nacionalidade')
            if nacionalidade == 'brasileiro':
                # Se brasileiro, CPF é obrigatório
                cpf = request_data.get('ciclista', {}).get('cpf')
                if not cpf:
                    return {"mensagem": 'CPF é obrigatório para brasileiros' }

            elif nacionalidade == 'estrangeiro':
                passaporte = request_data.get('ciclista', {}).get('passaporte', {})
                if not passaporte or not passaporte.get('numero') or not passaporte.get('validade') or not passaporte.get('pais'):
                    return {"mensagem" : 'Passaporte e país são obrigatórios para estrangeiros'}

            if not self.verifica_email(email):
                
                meio_de_pagamento_data = request_data.get('meioDePagamento', {})
                nome_titular = meio_de_pagamento_data.get('nome_titular')
                numero = meio_de_pagamento_data.get('numero')
                validade = meio_de_pagamento_data.get('validade')
                cvv = meio_de_pagamento_data.get('cvv')
                print(meio_de_pagamento_data)
                
                valida_cartao = self.valida_cartao(meio_de_pagamento_data)
                
                
                if(valida_cartao):
                    # Construir o objeto MeioDePagamento com o campo ciclista_id
                    ciclista_id = request_data.get('ciclista', {}).get('id_ciclista')
                    novo_meio_de_pagamento = MeioDePagamento(
                        nome_titular=nome_titular,
                        numero=numero,
                        validade=validade,
                        cvv=cvv,
                        ciclista=ciclista_id
                    )
                    novo_ciclista = Ciclista(**request_data.get('ciclista', {}))
                    self.ciclistas.append(novo_ciclista)
                    self.ciclistas = [Ciclista(**data) for data in self.ciclistas_data]
                    self.meio_de_pagamento_data.append(novo_meio_de_pagamento)
                    
                
                # chamar valida email 
                confirma_email= self.requisita_enviar_email("bqueiroz@edu.unirio.br","Confirmar Email", "Código:12345")
                if confirma_email:
                    return {'Ciclista cadastrado. Enviado email para ativação ' : request_data}
            else:
                return {"mensagem":'E-mail já cadastrado'}

        else:
            return {"mensagem":'Formato de e-mail inválido'}


    # chamar api microservice-externo
    def valida_cartao(self, request_data):
        # meio_de_pagamento = request_data.get('meioDePagamento', {})
        nome_titular = request_data.get('nome_titular')
        numero = request_data.get('numero')
        validade = request_data.get('validade')
        cvv = request_data.get('cvv')


        json_meio_de_pagamento = {
            "nome_titular": nome_titular,
            "numero": numero,
            "validade": validade,
            "cvv": cvv
        }


        # microservice-externo
        try: 
            url_valida_cartao = 'https://microservice-externo-b4i7jmshsa-uc.a.run.app/validaCartaoDeCredito'
            response = requests.post(url_valida_cartao, json=json_meio_de_pagamento)
            
            if response.status_code == 200:
                return True
            else:
                return False
            
        except requests.exceptions.RequestException as e:
            return {"error": f"Erro na solicitação: {e}"}



    def requisita_enviar_email(self, destinatario, assunto, mensagem): 
            url_email = "https://microservice-externo-b4i7jmshsa-uc.a.run.app/enviarEmail"
            
            dados = {"destinatario": "bqueiroz@edu.unirio.br", 
                    "assunto": assunto, 
                    "mensagem": mensagem
                    }
            try:
                response = requests.post(url_email, json = dados)
                response.raise_for_status()

            # confere se a requisição retorna um json
            except requests.exceptions.RequestException as e:
                return (f"Erro na requisição: {e}")
        
            if response.status_code == 200:
                return jsonify({"mensagem": "Requisição bem-sucedida"})
            else:
                return jsonify({"mensagem": "Erro na requisição", "status_code": response.status_code})

    def listar_todos(self):
        dados_ciclistas = {}
        for ciclista in self.ciclistas:
            dados_ciclista = ciclista.to_dict()
            meio_de_pagamento = next((mp for mp in self.meio_de_pagamento_data if mp["ciclista"] == ciclista.id_ciclista), None)
            dados_ciclista['meio_de_pagamento'] = meio_de_pagamento
            dados_ciclistas[ciclista.id_ciclista] = dados_ciclista
        return dados_ciclistas

    

    
    def verifica_email(self,email):
        for ciclista_data in self.ciclistas_data:
                    if ciclista_data["email"] == email:
                        return True       
        return False
    
    
    def permite_aluguel(self, id_ciclista):
        ciclista = self.obter_ciclista_por_id(id_ciclista)

        if ciclista is None:
            return {"error": "Ciclista não encontrado"}, 404

        if ciclista.status_aluguel == True:
            return False, 200
        
        return True,200
    
    
    def listar_meio_de_pagamento_por_id(self, id_ciclista):
        ciclista = self.obter_ciclista_por_id(id_ciclista)

        if ciclista is not None:
            for meio_de_pagamento_data in self.meio_de_pagamento_data:
                if meio_de_pagamento_data["ciclista"] == id_ciclista:
                    meio_de_pagamento_result = {
                        key: value for key, value in meio_de_pagamento_data.items() if key != "ciclista"
                    }
                    # Return only meio_de_pagamento data
                    return {"meio_de_pagamento": meio_de_pagamento_result}

            return {"mensagem": False, "message": "Ciclista sem cartão cadastrado"}
        else:
            return {"mensagem": False, "message": "Ciclista não encontrado."}
        

    

    def ativar_ciclista(self, id_ciclista):
        # TODO: Fazer ativação de emails
        ciclista = self.obter_ciclista_por_id(id_ciclista)
        if ciclista:
            ciclista.status = 'ativado'

            for i, ciclista_data in enumerate(self.ciclistas_data):
                if ciclista_data["id_ciclista"] == id_ciclista:
                    self.ciclistas_data[i].update({"status": "confirmado"})
                    break

            return {"ciclista ativado": ciclista.to_dict(include_status=False)}

        return {'mensagem': 'Ciclista não encontrado'}, 404




    def alterar_ciclista(self, id_ciclista, dados):
        ciclista = self.obter_ciclista_por_id(id_ciclista)
        
        if ciclista:
            # Atualiza apenas os atributos presentes nos dados
            ciclista.nome = dados.get("nome", ciclista.nome)
            ciclista.cpf = dados.get("cpf", ciclista.cpf)
            ciclista.passaporte = dados.get("passaporte", ciclista.passaporte)
            ciclista.nacionalidade = dados.get("nacionalidade", ciclista.nacionalidade)
            ciclista.url_foto_documento = dados.get("url_foto_documento", ciclista.url_foto_documento)
            ciclista.senha = dados.get("senha", ciclista.senha)

            # Validação dos dados
            if not self.validar_dados_ciclista(ciclista):
                return {"error": "Dados inválidos"}, 422
            
            # CHAMAR MICROSERVICE EMAIL
            # self.enviar_email()
            
        for ciclista_data in self.ciclistas_data:
            if ciclista_data["id_ciclista"] == id_ciclista:
                ciclista_data.update({
                    "nome": dados.get("nome", ciclista_data["nome"]),
                    "cpf": dados.get("cpf", ciclista_data["cpf"]),
                    "passaporte": dados.get("passaporte", ciclista_data["passaporte"]),
                    "nacionalidade": dados.get("nacionalidade", ciclista_data["nacionalidade"]),
                    "url_foto_documento": dados.get("url_foto_documento", ciclista_data["url_foto_documento"]),
                    "senha": dados.get("senha", ciclista_data["senha"]),
              
                })
                break
            
        for i, c in enumerate(self.ciclistas):
            if c.id_ciclista == id_ciclista:
                self.ciclistas[i] = ciclista.to_dict()
                break
            return ciclista.to_dict()        
        return {"error": "Ciclista não encontrado"}, 404


    def validar_dados_ciclista(self, ciclista):
        if ciclista.nacionalidade == "Brasileiro" and not ciclista.cpf:
            return False  
        return True
    
    
    def obter_ciclista_por_id(self, id_ciclista):
        for ciclista_data in self.ciclistas_data:
            if ciclista_data["id_ciclista"] == id_ciclista:
                return Ciclista(**ciclista_data)
        return None   
    
    def obter_ciclista_por_id_json(self, id_ciclista):
        for ciclista_data in self.ciclistas_data:
            if ciclista_data["id_ciclista"] == id_ciclista:
                ciclista = Ciclista(**ciclista_data)
                return ciclista.to_dict() 
        return None
    
