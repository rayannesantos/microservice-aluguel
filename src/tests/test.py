import unittest, os, sys
from unittest.mock import patch
from flask_testing import TestCase

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from controller.main import app
from service.AluguelService import AluguelService
from service.CiclistaService import CiclistaService
from service.FuncionarioService import FuncionarioService

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
        
           
   
if __name__ == '__main__':
    unittest.main()