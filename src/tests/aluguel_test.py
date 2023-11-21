import unittest
from unittest.mock import patch
from datetime import datetime
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
        
    def test_alterar_status_bicicleta(self):
        numero_bicicleta = 101
        novo_status = "Indisponível"

        self.aluguel_service.alterar_status_bicicleta(numero_bicicleta, novo_status)

        for bicicleta in self.aluguel_service.bicicletas:
            if bicicleta["numero"] == numero_bicicleta:
                self.assertEqual(bicicleta["status"], novo_status)
                break
        else:
            self.fail(f"Bicicleta com número {numero_bicicleta} não encontrada.")        

    def test_alterar_status_tranca(self):
        numero_tranca = 100
        novo_status = "Ocupada"

        tranca_simulada = {
            "id": 1,
            "bicicleta": 1,
            "numero": numero_tranca,
            "localizacao": "Estação A",
            "anoDeFabricacao": "2022",
            "modelo": "Tranca A",
            "status": self.aluguel_service.DISPONIVEL
        }
        self.aluguel_service.trancas.append(tranca_simulada)

        with patch.object(self.aluguel_service, 'trancas', [tranca_simulada]):
            self.aluguel_service.alterar_status_tranca(numero_tranca, novo_status)

        self.assertEqual(tranca_simulada["status"], novo_status)

    def test_devolver_bicicleta_invalido(self):
        numero_bicicleta = 1
        numero_tranca_devolucao = 105
        resultado, status_code = self.aluguel_service.devolver_bicicleta(numero_bicicleta, numero_tranca_devolucao)

        self.assertEqual(status_code, 404)

        
if __name__ == '__main__':
    
    unittest.main()
