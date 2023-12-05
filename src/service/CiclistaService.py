# UC01–Cadastrar Ciclista
from unittest.mock import Mock
from model.CiclistaModel import Ciclista
from model.MeiodePagamentoModel import MeioDePagamento  # Make sure to adjust the import path
import re
import requests
from flask import jsonify, Response


class CiclistaService: 
    def __init__(self):
        self.ciclistas_data = [
            {
                "id_ciclista": 3,
                "nome": "Ciclista 1",
                "nascimento": "nascimento",
                "cpf": "",
                "passaporte": {
                    "numero": "12358",
                    "validade": "02/01/1997",
                    "pais": "MX"
                },
                "nacionalidade": "ESTRANGEIRO",
                "email": "email@email.com.br",
                "url_foto_documento": "url_foto_documento",
                "senha": "senha"
            },
            {
                "id_ciclista": 4,
                "nome": "Ciclista 2",
                "nascimento": "nascimento",
                "cpf": "cpf",
                "passaporte": {
                    "numero": "passaporte_numero",
                    "validade": "passaporte_validade",
                    "pais": "passaporte_pais"
                },
                "nacionalidade": "nacionalidade",
                "email": "email",
                "url_foto_documento": "url_foto_documento",
                "senha": "senha"
            }
        ]
        self.ciclistas = [Ciclista(**data) for data in self.ciclistas_data]
        
        self.meio_de_pagamento_data = [
        {
            "nome_titular": "Titular",
            "numero_cartao": "1234567890123456",
            "validade_cartao": "2025-12-31",
            "cvv_cartao": "123",
            "ciclista":4
        },
        {
            "nome_titular": "Titular",
            "numero_cartao": "5234567890123456",
            "validade_cartao": "2035-12-31",
            "cvv_cartao": "423",
            "ciclista":3
        }                   
        ]


    def cadastrar_ciclista(self, request_data):
        email = request_data.get('ciclista', {}).get('email')
        meio_de_pagamento = request_data.get('meioDePagamento', {})
        print(meio_de_pagamento)
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
                
                novo_ciclista = Ciclista(**request_data.get('ciclista', {}))
                self.ciclistas.append(novo_ciclista)
                self.ciclistas = [Ciclista(**data) for data in self.ciclistas_data]
                
                # falta validar cartão e email
                # chamar microserviço validar cartão
                # adiciona pagamento
                meio_de_pagamento_data = request_data.get('meioDePagamento', {})
                nome_titular = meio_de_pagamento_data.get('nome_titular')
                numero_cartao = meio_de_pagamento_data.get('numero')
                validade_cartao = meio_de_pagamento_data.get('validade')
                cvv_cartao = meio_de_pagamento_data.get('cvv')

                # Construir o objeto MeioDePagamento com o campo ciclista_id
                ciclista_id = request_data.get('ciclista', {}).get('id_ciclista')
                novo_meio_de_pagamento = MeioDePagamento(
                    nome_titular=nome_titular,
                    numero_cartao=numero_cartao,
                    validade_cartao=validade_cartao,
                    cvv_cartao=cvv_cartao,
                    ciclista=ciclista_id
                )

                self.meio_de_pagamento_data.append(novo_meio_de_pagamento)
                
                # chamar valida email

                return {'Ciclista cadastrado ' : request_data}
            else:
                return {"mensagem":'E-mail já cadastrado'}

        else:
            return {"mensagem":'Formato de e-mail inválido'}


    # chamar api microservice-externo
    def valida_cartao(self, request_data):
        meio_de_pagamento = request_data.get('meioDePagamento', {})
        nome_titular = meio_de_pagamento.get('nomeTitular')
        numero_cartao = meio_de_pagamento.get('numero')
        validade_cartao = meio_de_pagamento.get('validade')
        cvv_cartao = meio_de_pagamento.get('cvv')

        json_meio_de_pagamento = {
            "nome_titular": nome_titular,
            "numero": numero_cartao,
            "validade": validade_cartao,
            "cvv": cvv_cartao
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
          return {"Erro na solicitação: {e}"}
          


    def listar_todos(self):
        ciclistas = [ciclista.to_dict() for ciclista in self.ciclistas]
        return ciclistas        
    
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
                    self.ciclistas_data[i].update({"status": "ativado"})
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
            self.enviar_email()
            
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
                return ciclista.to_dict()  # Retorna o dicionário JSON
        return None
    
   

    def validar_dados_cartao(self):
        # externo
        return True

    def enviar_para_administradora_cc(self):
        # Simulação do envio para a Administradora CC
        return True


    # Apenas para retornar sem chamar o microsserviço externo
    def enviar_email(self):
        return True
    
    # Apenas para retornar sem chamar o microsserviço externo
    def validar_cartao(self):
        return True
