# UC15 – Manter Cadastro de Funcionário

import random
from flask import Flask
from unittest.mock import Mock

requests = Mock()


def listar_funcionarios():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = [
        {
            "matricula": "123",
            "senha": "string",
            "confirmacaoSenha": "string",
            "email": "funcionarioum@example.com",
            "nome": "João João",
            "idade": 19,
            "funcao": "administrativa",
            "cpf": "string"
        },
        
         {
            "matricula": "456",
            "senha": "string",
            "confirmacaoSenha": "string",
            "email": "funcionariodois@example.com",
            "nome": "Maria Maria",
            "idade": 18,
            "funcao": "reparador",
            "cpf": "string"
        },
            
            
    ]

    return response_mock.json()