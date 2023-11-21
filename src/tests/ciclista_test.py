import unittest
from unittest.mock import patch
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.CiclistaService import CiclistaService
from model.CiclistaModel import Ciclista


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

        # Mock para a função de envio de e-mail para evitar a execução real durante os testes
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





if __name__ == '__main__':
    unittest.main()
