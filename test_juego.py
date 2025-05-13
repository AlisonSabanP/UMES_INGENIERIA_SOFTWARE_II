import unittest
from juego import comparar_jugada, jugar_partida
import unittest
from juego import comparar_jugada

class TestCompararJugada(unittest.TestCase):
    def test_piedra_vs_piedra(self):
        result = comparar_jugada("piedra", "piedra")
        self.assertEqual(result, 0)
    
    def test_piedra_vs_papel(self):
        result = comparar_jugada("piedra", "papel")
        self.assertEqual(result, -1)
    
    def test_piedra_vs_tijera(self):
        result = comparar_jugada("piedra", "tijera")
        self.assertEqual(result, 1)
    
    def test_papel_vs_piedra(self):
        result = comparar_jugada("papel", "piedra")
        self.assertEqual(result, 1)
    
    def test_papel_vs_papel(self):
        result = comparar_jugada("papel", "papel")
        self.assertEqual(result, 0)
    
    def test_papel_vs_tijera(self):
        result = comparar_jugada("papel", "tijera")
        self.assertEqual(result, -1)
    
    def test_tijera_vs_piedra(self):
        result = comparar_jugada("tijera", "piedra")
        self.assertEqual(result, -1)
    
    def test_tijera_vs_papel(self):
        result = comparar_jugada("tijera", "papel")
        self.assertEqual(result, 1)
    
    def test_tijera_vs_tijera(self):
        result = comparar_jugada("tijera", "tijera")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()