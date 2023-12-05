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
            "confirmacaoSenha": "123",
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
    