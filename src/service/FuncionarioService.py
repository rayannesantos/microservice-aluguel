# UC15 – Manter Cadastro de Funcionário

import random
from flask import Flask
from unittest.mock import Mock
from  model.FuncionarioModel import Funcionario

requests = Mock()

class FuncionarioService: 
    def __init__(self):
        self.funcionarios_data = [
            {
                "id_funcionario":1,
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
                "id_funcionario":2,
                "matricula": "456",
                "senha": "string",
                "confirmacaoSenha": "string",
                "email": "funcionariodois@example.com",
                "nome": "Maria Maria",
                "idade": 18,
                "funcao": "reparador",
                "cpf": "string"
            }
        ]

        self.funcionarios = [Funcionario(**data) for data in self.funcionarios_data]
        
    def listar_todos_funcionarios(self):
        funcionarios = [funcionario.to_dict() for funcionario in self.funcionarios]
        return funcionarios

    def obter_funcionario_por_id(self, id_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                return funcionario
        return None

    def obter_funcionario_por_id_json(self, id_funcionario):
        for funcionario_data in self.funcionarios_data:
            if funcionario_data['id_funcionario'] == id_funcionario:
                print(f"Encontrado funcionário com ID {id_funcionario}")
                funcionario = Funcionario(**funcionario_data)
                return funcionario.to_dict()
        print("não foi {id_funcionario}")
        return None
    
    def remover_funcionario_por_id(self, id_funcionario):
        funcionario = next((f for f in self.funcionarios_data if f["id_funcionario"] == id_funcionario), None)
        if funcionario:
            self.funcionarios_data.remove(funcionario)
            self.funcionarios = [Funcionario(**data) for data in self.funcionarios_data]
            return True
        return False
    
    
    

    # def obter_ciclista_por_id_json(self, id_ciclista):
    #     for ciclista_data in self.ciclistas_data:
    #         if ciclista_data["id_ciclista"] == id_ciclista:
    #             ciclista = Ciclista(**ciclista_data)
    #             return ciclista.to_dict()  # Retorna o dicionário JSON
    #     return None

    # def listar_funcionarios():
    #     response_mock = Mock()
    #     response_mock.status_code = 200
    #     response_mock.json.return_value = [
    #         {
    #             "id_funcionario":1,
    #             "matricula": "123",
    #             "senha": "string",
    #             "confirmacaoSenha": "string",
    #             "email": "funcionarioum@example.com",
    #             "nome": "João João",
    #             "idade": 19,
    #             "funcao": "administrativa",
    #             "cpf": "string"
    #         },
            
    #         {
    #             "id_funcionario":2,
    #             "matricula": "456",
    #             "senha": "string",
    #             "confirmacaoSenha": "string",
    #             "email": "funcionariodois@example.com",
    #             "nome": "Maria Maria",
    #             "idade": 18,
    #             "funcao": "reparador",
    #             "cpf": "string"
    #         },    
    #     ]
    #     return response_mock.json()

    # def listar_funcionario_id (id_funcionario):
    #     response_mock = Mock()
    #     response_mock.status_code = 200
    
    #     funcionarios = listar_funcionarios()
        
    #     for funcionario in funcionarios:
    #         print(funcionario)
    #         if funcionario['id_funcionario'] == id_funcionario:
    #             return funcionario

    #     response_mock.status_code = 404
    #     response_mock.json.return_value = [
    #         {
    #             "codigo": 404,
    #             "mensagem": "Not found"
    #         }
    #     ]
    #     return response_mock.json()
        

    # def cadastrar_funcionario(senha, confirmacao_senha, email, nome, idade, funcao, cpf):
    #     response_mock = Mock()
    #     response_mock.status_code = "Dados cadastrados", 200
        
    #     validacao = True
    #     if validacao == False:
    #         response_mock.status_code = 422
    #         response_mock.json.return_value = [
    #             {
    #                 "codigo": 422,
    #                 "mensagem": "Dados inválidos"
    #             }
    #         ]
    #         return response_mock.json()
        
    #     else:
    #         response_mock.json.return_value = {
    #             "id_funcionario":3,
    #             "matricula":567,
    #             "senha" : senha,
    #             "confirmacao_senha": confirmacao_senha,
    #             "email" : email,
    #             "nome" : nome,
    #             "idade" : idade,
    #             "funcao" : funcao,
    #             "cpf" : cpf  
    #         }
    #         return response_mock.json()
    
    
    # def editar_funcionario(id_funcionario, senha, confirmacao_senha, email, nome, idade, funcao, cpf ):

    #     response_mock = Mock()
    #     response_mock.status_code = "Dados editados", 200
        
    #     funcionario = listar_funcionario_id(id_funcionario)
        
    #     if funcionario:
    #         response_mock.status_code = 200
    #         response_mock.json.return_value = {
    #             "senha": senha,
    #             "confirmacaoSenha": confirmacao_senha,
    #             "email": email,
    #             "nome": nome,
    #             "idade": idade,
    #             "funcao": funcao,
    #             "cpf": cpf
    #         }
    #         return response_mock.json()
    #     else:
    #         response_mock.status_code = 404
    #         response_mock.json.return_value = {"error": "Funcionário não encontrado"}
    #         return response_mock.json()
    

    # def remover_funcionario(id_funcionario):
    #     response_mock = Mock()

    #     funcionarios = listar_funcionarios()
    #     index_to_remove = None
    #     for i, funcionario in enumerate(funcionarios):
    #         if funcionario['id_funcionario'] == id_funcionario:
    #             index_to_remove = i
    #             break

    #     if index_to_remove is not None:
    #         del funcionarios[index_to_remove]
    #         response_mock.status_code = 200
    #         response_mock.json.return_value = {"message": "Funcionário removido com sucesso"}
    #     else:
    #         response_mock.status_code = 404
    #         response_mock.json.return_value = {"error": "Funcionário não encontrado"}

    #     return response_mock.json()