import unittest, os, sys
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app

class TestMain(unittest.TestCase):

    @patch('controller.main.Mock')
    def test_listar_ciclista_route(self, mock_listar_ciclista):

        mock_listar_ciclista.status_code = 200

        with app.test_client() as client:
            response = client.get('/ciclistas')
            self.assertEqual(response.status_code, mock_listar_ciclista.status_code)

    @patch('controller.main.Mock')
    def test_cadastrar_ciclista_route(self, mock_cadastrar_ciclista):

        mock_cadastrar_ciclista.status_code = 200

        data = {
            "ciclista": {
                "id_ciclista": 3,
                "nome": "nome",
                "nascimento": "nascimento",
                "cpf": "cpf",
                "passaporte": {
                    "numero": "passaporte_numero",
                    "validade": "passaporte_validade",
                    "pais": "passaporte_pais"
                },
                "nacionalidade": "nacionalidade",
                "email": "email",
                "url_foto_documento": "url_foto_documento",
                "senha": "senha"
            },
            "meio_de_pagamento": {
                "nome_titular": "nome_titular",
                "numero": "numero_cartao",
                "validade": "validade_cartao",
                "cvv": "cvv"
            }
        }

        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.post('/ciclista', json=data, headers={"Content-Type": "application/json", "X-CSRFToken": token})
            self.assertEqual(response.status_code, mock_cadastrar_ciclista.status_code)

    @patch('controller.main.Mock')
    def test_ativar_ciclista_route(self, mock_ativar_ciclista):

        mock_ativar_ciclista.status_code = 200

        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.post('/ciclista/1/ativar', headers={"Content-Type": "application/json", "X-CSRFToken": token})
            self.assertEqual(response.status_code, mock_ativar_ciclista.status_code)

    @patch('controller.main.Mock')
    def test_listar_funcionarios_route(self, mock_listar_funcionarios):

        mock_listar_funcionarios.status_code = 200

        with app.test_client() as client:
            response = client.get('/funcionarios')
            self.assertEqual(response.status_code, mock_listar_funcionarios.status_code)


    @patch('controller.main.Mock')
    def test_cadastrar_funcionario_route(self, mock_cadastrar_funcionario):

        mock_cadastrar_funcionario.status_code = 200

        data = {
            "id_funcionario":1,
            "matricula": "teste",
            "senha": "teste",
            "confirmacaoSenha": "teste",
            "email": "teste@example.com",
            "nome": "teste",
            "idade": 19,
            "funcao": "REPARADOR",
            "cpf": "teste"
        }

        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.post('/funcionario', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_cadastrar_funcionario.status_code)


    @patch('controller.main.Mock')
    def test_editar_funcionario_route(self, mock_editar_funcionario):

        mock_editar_funcionario.status_code = 200

        data = {
            "id_funcionario": 2,
            "matricula": "teste",
            "senha": "teste",
            "confirmacaoSenha": "teste",
            "email": "teste@example.com",
            "nome": "teste",
            "idade": 19,
            "funcao": "REPARADOR",
            "cpf": "teste"
        }

        token = "None"
        with app.test_client() as client:
            response = client.get('/get_csrf_token')
            token = response.get_data(as_text=True)
            response = client.put('/funcionario/2', headers={"Content-Type": "application/json", "X-CSRFToken": token}, json=data)
            self.assertEqual(response.status_code, mock_editar_funcionario.status_code) 

if __name__ == '__main__':
    unittest.main()