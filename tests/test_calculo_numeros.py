import unittest
from src.exceptions import (
    ingrese_numero, NumeroDebeSerPositivo
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

    @patch(   'builtins.input',return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch(   'builtins.input',return_value='-50')
    def test_ingreso_negativo1(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch(   'builtins.input',return_value='-10')
    def test_ingreso_negativo2(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch(   'builtins.input',return_value='-5')
    def test_ingreso_negativo3(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch(   'builtins.input',return_value='-1')
    def test_ingreso_negativo4(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
            

if __name__ == '__main__':
    unittest.main() 