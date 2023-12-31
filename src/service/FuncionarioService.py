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
            "matricula": "12345",
            "senha": "123",
            "confirmacao_senha": "123",
            "email": "employee@example.com",
            "nome": "Beltrano",
            "idade": 25,
            "funcao": "Reparador",
            "cpf": "99999999999"
            }
        ]

        self.funcionarios = [Funcionario(**data) for data in self.funcionarios_data]
        
    def listar_todos_funcionarios(self):
        funcionarios = [funcionario.to_dict() for funcionario in self.funcionarios]
        return funcionarios


    def cadastrar_funcionario(self, request_data):
            novo_funcionario = Funcionario(**request_data)
            self.funcionarios.append(novo_funcionario)
            return {'Funcionario cadastrado. ' : request_data}
                    
    def alterar_funcionario(self, id_funcionario, dados):
        funcionario = self.obter_funcionario_por_id(id_funcionario)
        if funcionario:
            funcionario.matricula = dados.get('matricula', funcionario.matricula)
            funcionario.senha = dados.get('senha', funcionario.senha)
            funcionario.confirmacao_senha = dados.get('confirmacao_senha', funcionario.confirmacao_senha)
            funcionario.email = dados.get('email', funcionario.email)
            funcionario.nome = dados.get('nome', funcionario.nome)
            funcionario.idade = dados.get('idade', funcionario.idade)
            funcionario.funcao = dados.get('funcao', funcionario.funcao)
            funcionario.cpf = dados.get('cpf', funcionario.cpf)
            return {'mensagem': 'Funcionário alterado com sucesso', 'funcionario': funcionario.to_dict()}
  
        return {'Funcionário não encontrado'}
                       

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
    