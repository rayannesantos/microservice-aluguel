# UC01–Cadastrar Ciclista

import random
from flask import Flask
from unittest.mock import Mock

app = Flask(__name__)


def cadastrar_ciclista(nome, nascimento, cpf, passaporteNumero, passaporteValidade, passaportePais, nacionalidade, email, 
                       urlFotoDocumento,senha, nomeTitular, numeroCartao, validadeCartao, cvv ):
    
    # TODO validarEmail
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
    
    response_mock.json.return_value = {
        "ciclista": {
            # TODO validação para apenas numeros que não foram usados
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

    return response_mock.json()


