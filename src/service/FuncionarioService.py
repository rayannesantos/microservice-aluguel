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

def cadastrar_funcionario(senha, confirmacaoSenha, email, nome, idade, funcao, cpf ):
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
        "matricula":567,
        "senha" : senha,
         "confirmacaoSenha":confirmacaoSenha,
        "email" : email,
        "nome" : nome,
        "idade" : idade,
        "funcao" : funcao,
        "cpf" : cpf
            
     }
        
     return response_mock.json()

# TODO editarFuncionario
# TODO deletarFuncionario