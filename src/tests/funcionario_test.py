import unittest, os, sys
from unittest.mock import patch, Mock

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.FuncionarioService import listar_funcionarios,listar_funcionario_id, cadastrar_funcionario, editar_funcionario,remover_funcionario

class TestBicicletaService(unittest.TestCase):
    @patch('service.FuncionarioService.Mock')
    def test_listar_funcionarios(self, mock_request):
        
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = [
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
            },    
        ]
        

        mock_request.return_value = response_mock

        result = listar_funcionarios()
        self.assertEqual(len(result), 2) 

