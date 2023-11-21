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


    @patch('service.FuncionarioService.Mock')
    def test_cadastrar_funcionario(self, mock_request):
        senha, confirmacao_senha, email, nome, idade, funcao, cpf  = "123","123", "teste@email.com","Teste" ,30, "REPARADOR", "85459341060"
        response_mock = Mock()
        response_mock.status_code = 200

        response_mock.json.return_value = {
            "id_funcionario": 3,
            "matricula":"567",
            "senha" : senha,
            "confirmacaoSenha":confirmacao_senha,
            "email" : email,
            "nome" : nome,
            "idade" : idade,
            "funcao" : funcao,
            "cpf" : cpf
        }
        mock_request.return_value = response_mock
        result = cadastrar_funcionario(senha, confirmacao_senha, email, nome, idade, funcao, cpf)
        self.assertEqual(result['email'], email)  
        self.assertEqual(result['cpf'], cpf)

if __name__ == '__main__':
    unittest.main()