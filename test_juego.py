import unittest
from juego import comparar_jugada, jugar_partida
import unittest
from juego import comparar_jugada

class TestCompararJugada(unittest.TestCase):
    def test_piedrapiedra(self):
        result = comparar_jugada("cuadrado", "piedra")
        self.assertEqual(result, 0)
    
    def test_piedrapapel(self):
        result = comparar_jugada("piedra", "papel")
        self.assertEqual(result, -1)
    
    def test_piedratijera(self):
        result = comparar_jugada("piedra", "tijera")
        self.assertEqual(result, 1)
    
    def test_papelpiedra(self):
        result = comparar_jugada("papel", "piedra")
        self.assertEqual(result, 1)
    
    def test_papelpapel(self):
        result = comparar_jugada("papel", "papel")
        self.assertEqual(result, 0)
    
    def test_papeltijera(self):
        result = comparar_jugada("papel", "tijera")
        self.assertEqual(result, -1)
    
    def test_tijerapiedra(self):
        result = comparar_jugada("tijera", "piedra")
        self.assertEqual(result, -1)
    
    def test_tijerapapel(self):
        result = comparar_jugada("tijera", "papel")
        self.assertEqual(result, 1)
    
    def test_tijeratijera(self):
        result = comparar_jugada("tijera", "tijera")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()