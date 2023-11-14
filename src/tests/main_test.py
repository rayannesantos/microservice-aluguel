import unittest, os, sys
from unittest.mock import patch

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app

class TestMain(unittest.TestCase):

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
        with app.test_client() as client:
            response = client.post('/funcionario', headers={"Content-Type": "application/json"}, json=data)
            self.assertEqual(response.status_code, mock_cadastrar_funcionario.status_code)

if __name__ == '__main__':
    unittest.main()