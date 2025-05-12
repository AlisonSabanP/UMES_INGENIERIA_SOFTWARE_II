import unittest
from juego import comparar_jugada, jugar_partida

class TestJuego(unittest.TestCase):

    def test_comparar_jugada(self):
        self.assertEqual(comparar_jugada('piedra', 'tijera'), 1)
        self.assertEqual(comparar_jugada('piedra', 'papel'), -1)
        self.assertEqual(comparar_jugada('piedra', 'piedra'), 0)

        self.assertEqual(comparar_jugada('papel', 'piedra'), 1)
        self.assertEqual(comparar_jugada('papel', 'tijera'), -1)
        self.assertEqual(comparar_jugada('papel', 'papel'), 0)

        self.assertEqual(comparar_jugada('tijera', 'papel'), 1)
        self.assertEqual(comparar_jugada('tijera', 'piedra'), -1)
        self.assertEqual(comparar_jugada('tijera', 'tijera'), 0)

    def test_jugar_partida(self):
        self.assertEqual(jugar_partida(['piedra', 'papel', 'tijera'], ['tijera', 'piedra', 'papel']), 'Humano')

        self.assertEqual(jugar_partida(['piedra', 'papel', 'tijera'], ['papel', 'tijera', 'piedra']), 'Programa')

        self.assertEqual(jugar_partida(['piedra', 'papel', 'tijera'], ['piedra', 'papel', 'tijera']), 'Empate')

if __name__ == '__main__':
    unittest.main()
