import unittest
from src.exceptions import (
    ingrese_numero
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(   'builtins.input',return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
        
    @patch(   'builtins.input',return_value='50')
    def test_ingreso_feliz1(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 50)

    @patch(   'builtins.input',return_value='10')
    def test_ingreso_feliz2(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 10)

    @patch(   'builtins.input',return_value='5')
    def test_ingreso_feliz3(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 5)

    @patch(   'builtins.input',return_value='1')
    def test_ingreso_feliz4(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 1)

if __name__ == '__main__':
    unittest.main() 