import unittest, os, sys
from unittest.mock import patch
from flask_testing import TestCase

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app, enviar_email , obter_tranca , obter_bicicleta, chamar_cobranca


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
        self.assertEqual(response.status_code, 200)

    def test_aluguel_route(self):         
        data = {
        "id_ciclista": 2,
        "tranca_inicio": 2
        } 
        response = self.client.post('/aluguel', json=data)
        self.assertEqual(response.status_code, 200)

    def test_devolucao_route(self):         
        data = {
        "id_tranca": 2,
        "id_bicicleta": 1
        } 
        response = self.client.post('/devolucao', json=data)
        self.assertEqual(response.status_code, 200)  


    @patch('controller.main.enviar_email')
    def test_enviar_email_integration(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"status": "success"}

        resultado = enviar_email("Teste", "Isso é um teste")

        self.assertTrue(resultado)

    @patch('controller.main.obter_tranca')
    def test_obter_tranca_integration(self, mock_get):
        mock_get.return_value.status_code = 200
        resultado = obter_tranca(1)
        
        self.assertEqual(resultado.status_code, 200)


    @patch('controller.main.obter_bicicleta')
    def test_obter_bicicleta_integration(self, mock_get):
        mock_get.return_value.status_code = 200
        resultado = obter_bicicleta(0)
        self.assertEqual(resultado.status_code, 200)

    @patch('controller.main.chamar_cobranca')
    def test_obter_bicicleta_integration(self, mock_get):
        mock_get.return_value.status_code = 200
        resultado = chamar_cobranca(3)
        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()