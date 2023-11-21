import unittest
from unittest.mock import patch
from flask import Flask, json
from werkzeug.exceptions import NotFound

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.AluguelController import aluguel_app

class TestAluguelRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(aluguel_app, url_prefix='/aluguel')
        self.client = self.app.test_client()

    @patch('controller.AluguelController.aluguel_service.alugar_bicicleta')
    def test_alugar_bicicleta_route(self, mock_alugar_bicicleta):
        mock_alugar_bicicleta.return_value = {'status': 'success'}

        data = {'id_ciclista': 1, 'trancaInicio': '123'}
        response = self.client.post('/aluguel/', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'success'})
        mock_alugar_bicicleta.assert_called_with(1, '123')

    @patch('controller.AluguelController.aluguel_service.obter_aluguel_por_bicicleta')
    def test_listar_aluguel_route(self, mock_obter_aluguel_por_bicicleta):
        mock_obter_aluguel_por_bicicleta.return_value = {'status': 'success'}

        response = self.client.get('/aluguel/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'success'})
        mock_obter_aluguel_por_bicicleta.assert_called_with(1)

    @patch('controller.AluguelController.aluguel_service.devolver_bicicleta')
    def test_devolver_bicicleta_route(self, mock_devolver_bicicleta):
        mock_devolver_bicicleta.return_value = {'status': 'success'}

        data = {'idTranca': '456', 'idBicicleta': 1}
        response = self.client.post('/aluguel/devolucao', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'success'})
        mock_devolver_bicicleta.assert_called_with(1, '456')

    def test_invalid_route(self):
        response = self.client.get('/aluguel/invalid_route/')

        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
