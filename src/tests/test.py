import unittest, os, sys
from unittest.mock import patch
from flask_testing import TestCase

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app
from service.AluguelService import AluguelService
from service.CiclistaService import CiclistaService
from service.FuncionarioService import FuncionarioService

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
    
    def test_listar_ciclista_id_route(self):
        response = self.client.get('/ciclista/1')
        self.assertEqual(response.status_code, 200)
        
    def test_listar_meio_de_pagamento_route(self):
        response = self.client.get('/cartaoDeCredito/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_listar_todos_os_ciclistas_route(self):
        response = self.client.get('/allciclistas')
        self.assertEqual(response.status_code, 200)
             
    def test_listar_todos_os_funcionarios_route(self):
        response = self.client.get('/funcionario')
        self.assertEqual(response.status_code, 200)    
        
    def test_listar_todos_funcionarios_id_route(self):
        response = self.client.get('/funcionario/1')
        self.assertEqual(response.status_code, 200)  
        
        
    def test_cadastrar_ciclista_route(self):         
        data = {
            "ciclista": {
                "id_ciclista":1,
                "nome": "string",
                "nascimento": "2023-12-05",
                "cpf": "44286496753",
                "passaporte": {
                "numero": "string",
                "validade": "2023-12-05",
                "pais": "JM"
                },
                "nacionalidade": "string",
                "email": "user20@example.com",
                "url_foto_documento": "string",
                "senha": "string"
            },
            "meioDePagamento": {
                "nome_titular": "string",
                "numero": "2459398914097794571835616046632677",
                "validade": "2023-12-05",
                "cvv": "307"
            }
        }  
        response = self.client.post('/ciclista', json=data)
        print(response)
        self.assertEqual(response.status_code, 200)
           
           
    def test_cadastrar_funcionario_route(self):         
        data = {
            "id_funcionario":50,
             "matricula": 4435698,
            "senha": "string",
            "confirmacao_senha": "string",
            "email": "user@example.com",
            "nome": "string",
            "idade": 0,
            "funcao": "string",
            "cpf": "string"
        }  
        response = self.client.post('/funcionario', json=data)
        print(response)
        self.assertEqual(response.status_code, 200)
   
if __name__ == '__main__':
    unittest.main()