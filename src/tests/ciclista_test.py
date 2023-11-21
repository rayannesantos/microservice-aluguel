import unittest
from unittest.mock import patch,Mock
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.CiclistaService import CiclistaService
from model.CiclistaModel import Ciclista
from model.MeiodePagamentoModel import MeioDePagamento


class TestCiclistaService(unittest.TestCase):
    def setUp(self):
        self.ciclista_service = CiclistaService()

    def test_alterar_ciclista(self):
        # Teste para alterar dados de um ciclista com dados válidos
        id_ciclista = 3
        novos_dados = {
            "nome": "Novo Nome",
            "cpf": "123456789",
            "passaporte": {
                "numero": "987654321",
                "validade": "01/01/2023",
                "pais": "BR"
            },
            "nacionalidade": "BRASILEIRO",
            "url_foto_documento": "nova_url",
            "senha": "nova_senha"
        }

        with patch.object(self.ciclista_service, 'enviar_email') as mock_enviar_email:
            resultado = self.ciclista_service.alterar_ciclista(id_ciclista, novos_dados)

        # Verificando se os dados foram atualizados corretamente
        self.assertEqual(resultado["nome"], novos_dados["nome"])
        self.assertEqual(resultado["cpf"], novos_dados["cpf"])
        self.assertEqual(resultado["passaporte"], novos_dados["passaporte"])
        self.assertEqual(resultado["nacionalidade"], novos_dados["nacionalidade"])
        self.assertEqual(resultado["url_foto_documento"], novos_dados["url_foto_documento"])
        self.assertEqual(resultado["senha"], novos_dados["senha"])

        # Verificando se a função de envio de e-mail foi chamada
        mock_enviar_email.assert_called_once()

    def test_alterar_cartao(self):
        # Teste para alterar os dados do cartão de um ciclista
        id_ciclista =  4 # Substitua pelo ID válido do ciclista
        dados_cartao = {
            "nome_titular": "Novo Titular",
            "numero_cartao": "1234567812345678",
            "validade_cartao": "12/25",
            "cvv_cartao": "123"
        }

        # Mock para a função de envio de e-mail e para a validação junto à administradora de cartão
        with patch.object(self.ciclista_service, 'enviar_email') as mock_enviar_email, \
                patch.object(self.ciclista_service, 'enviar_para_administradora_cc', return_value=True) as mock_enviar_para_administradora_cc:

            resultado = self.ciclista_service.alterar_cartao(id_ciclista, dados_cartao)

        self.assertIsInstance(resultado, dict)

        # Verificando se os dados do cartão foram atualizados corretamente
        if "error" in resultado:
            self.fail(f"Erro inesperado: {resultado['error']}")
        elif "success" in resultado:
            self.assertEqual(resultado["success"], "Cartão atualizado com sucesso")
        elif "warning" in resultado:
            self.assertEqual(resultado["warning"], "Cartão atualizado, mas houve um problema ao enviar o e-mail")
        else:
            self.fail("Chave 'error', 'success' ou 'warning' não encontrada no resultado")

        # Verificando se as funções de envio de e-mail e administradora foram chamadas
        mock_enviar_email.assert_called_once()
        mock_enviar_para_administradora_cc.assert_called_once()



    def test_ativar_ciclista(self):
        response_mock = Mock()
        response_mock.status_code = 200

        ciclistas = [
            {'id_ciclista': 1, 'status': 'pendente'},
            {'id_ciclista': 2, 'status': 'pendente'},
            {'id_ciclista': 3, 'status': 'pendente'},
        ]
        self.ciclista_service.listar_ciclistas = Mock(return_value=ciclistas)

        ciclista_id = 2
        resultado = self.ciclista_service.ativar_ciclista(ciclista_id)

        self.assertEqual(resultado['status'], 'ativado')

    def test_listar_meio_de_pagamento_por_id_found(self):
        id_ciclista =  4 
        dados_cartao = {
            "nome_titular": "Novo Titular",
            "numero_cartao": "1234567812345678",
            "validade_cartao": "12/25",
            "cvv_cartao": "123",
            "ciclista": 4
        }
                
        with patch.object(self.ciclista_service, 'enviar_email') as mock_enviar_email, \
                patch.object(self.ciclista_service, 'enviar_para_administradora_cc', return_value=True) as mock_enviar_para_administradora_cc:

            resultado = self.ciclista_service.alterar_cartao(id_ciclista, dados_cartao)

        self.assertIsInstance(resultado, dict)          


if __name__ == '__main__':
    unittest.main()
