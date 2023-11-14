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


if __name__ == '__main__':
    unittest.main()