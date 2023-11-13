# UC01–Cadastrar Ciclista

import random
from flask import Flask
from unittest.mock import Mock

app = Flask(__name__)


def cadastrar_ciclista(nome, nascimento, cpf, passaporte_numero, passaporte_validade, passaporte_pais, nacionalidade, email, 
                       url_foto_documento,senha, nome_titular, numero_cartao, validade_cartao, cvv ):
    
    response_mock = Mock()
    response_mock.status_code = "Dados cadastrados", 200

    validacao = True
    
    if not validacao:
        response_mock.status_code = 422
        response_mock.json.return_value = [
            {
                "codigo": 422,
                "mensagem": "Dados inválidos"
            }
        ]
        return response_mock.json()
    
    else:
        validar_cartao()
        
        response_mock.json.return_value = {
            "ciclista": {
                "id_ciclista": random.randint(1, 1000),
                "nome": nome,
                "nascimento": nascimento,
                "cpf": cpf,
                "passaporte": {
                    "numero": passaporte_numero,
                    "validade": passaporte_validade,
                    "pais": passaporte_pais
                },
                "nacionalidade": nacionalidade,
                "email": email,
                "urlFotoDocumento": url_foto_documento,
                "senha": senha
            },
            "meioDePagamento": {
                "nomeTitular": nome_titular,
                "numero": numero_cartao,
                "validade": validade_cartao,
                "cvv": cvv
            }
        }
        

        enviar_email()
        return response_mock.json()


# UC02 – Confirmar email
def ativar_ciclista (id_ciclista):
    response_mock = Mock()
    response_mock.status_code = 200
   
    ciclistas = listar_ciclistas()
    for ciclista in ciclistas:
        if ciclista['id_ciclista'] == id_ciclista:
            ciclista['status'] = 'ativado'
            return ciclista

    return {'error': 'Ciclista not found'}, 404
    


def listar_ciclistas():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = [
       {
        "id_ciclista": 1,
        "status": "desativado",
        "nome": "string",
        "nascimento": "2023-11-13",
        "cpf": "00964211258",
        "passaporte": {
            "numero": "string",
            "validade": "2023-11-13",
            "pais": "JF"
        },
        "nacionalidade": "string",
        "email": "user@example.com",
        "urlFotoDocumento": "string"
        },   
      {
        "id_ciclista": 2,
        "status": "desativado",
        "nome": "string",
        "nascimento": "2023-11-13",
        "cpf": "00964211258",
        "passaporte": {
            "numero": "string",
            "validade": "2023-11-13",
            "pais": "JF"
        },
        "nacionalidade": "string",
        "email": "user@example.com",
        "urlFotoDocumento": "string"
      },   
    ]
    return response_mock.json()




# método de enviar email (retornando sempre "sucesso"), mas que não chame o microsserviço Externo. 
def enviar_email():
    response_mock = Mock()
    response_mock.json.return_value = {"message": "Email enviado com sucesso"}
    return response_mock.json()

# Apenas para retornar sem chamar o microsserviço externo
def validar_cartao():
    return True



