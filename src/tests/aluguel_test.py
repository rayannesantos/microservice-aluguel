import unittest
from unittest.mock import patch
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.AluguelService import AluguelService
from model.AluguelModel import AluguelBicicleta

class TestAluguelService(unittest.TestCase):
    def setUp(self):
        self.aluguel_service = AluguelService()

    def test_alugar_bicicleta(self):
        id_ciclista = 4
        numero_tranca = 100
        resultado,status_code= self.aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
        self.assertEqual(status_code, 200)

    def test_alugar_bicicleta_invalido_ciclista(self):
        id_ciclista = 5
        numero_tranca = 100
        resultado,status_code= self.aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
        self.assertEqual(status_code, 404)

    def test_alugar_bicicleta_invalido_tranca(self):
        id_ciclista = 4
        numero_tranca = 102
        resultado,status_code= self.aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
        self.assertEqual(status_code, 404)

    def test_alugar_bicicleta_invalido_tranca_e_ciclista(self):
        id_ciclista = 5
        numero_tranca = 102
        resultado,status_code= self.aluguel_service.alugar_bicicleta(id_ciclista, numero_tranca)
        self.assertEqual(status_code, 404)

if __name__ == '__main__':
    unittest.main()