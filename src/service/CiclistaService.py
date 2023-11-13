# UC01–Cadastrar Ciclista

import random
from flask import Flask
from unittest.mock import Mock

app = Flask(__name__)


def cadastrar_ciclista(nome, nascimento, cpf, passaporteNumero, passaporteValidade, passaportePais, nacionalidade, email, 
                       urlFotoDocumento,senha, nomeTitular, numeroCartao, validadeCartao, cvv ):
    
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
    
    validar_cartao()
    
    response_mock.json.return_value = {
        "ciclista": {
            "id": random.randint(1, 1000),
            "nome": nome,
            "nascimento": nascimento,
            "cpf": cpf,
            "passaporte": {
                "numero": passaporteNumero,
                "validade": passaporteValidade,
                "pais": passaportePais
            },
            "nacionalidade": nacionalidade,
            "email": email,
            "urlFotoDocumento": urlFotoDocumento,
            "senha": senha
        },
        "meioDePagamento": {
            "nomeTitular": nomeTitular,
            "numero": numeroCartao,
            "validade": validadeCartao,
            "cvv": cvv
        }
    }
    

    enviar_email()
    return response_mock.json()


# método de enviar email (retornando sempre "sucesso"), mas que não chame o microsserviço Externo. 
def enviar_email():
    response_mock = Mock()
    response_mock.json.return_value = {"message": "Email enviado com sucesso"}
    return response_mock.json()

# Apenas para retornar sem chamar o microsserviço externo
def validar_cartao():
    return True



