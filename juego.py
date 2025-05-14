import random
import sys

def comparar_jugada(jugadaH, jugadaM):
    jugadaH = jugadaH.lower()
    jugadaM = jugadaM.lower()

    if jugadaH == jugadaM:
        return 0
    elif (jugadaH == 'roca' and jugadaM == 'tijera') or \
        (jugadaH == 'tijera' and jugadaM == 'papel') or \
        (jugadaH == 'papel' and jugadaM == 'piedra'):
        return 1
    else:
        return -1

def jugar_partida(listaH, listaM):
    resultadoH = 0
    resultadoM = 0
    for i in range(3):
        resultado = comparar_jugada(listaH[i], listaM[i])
        if resultado == 1:
            resultadoH += 1
        elif resultado == -1:
            resultadoM += 1

    print('Punteo:', resultadoH, '-', resultadoM)
    if resultadoH > resultadoM:
        return "Humano"
    elif resultadoH < resultadoM:
        return "Programa"
    else:
        return "Empate"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python juego.py [jugada1] [jugada2] [jugada3]")
        sys.exit(1)

    listaH = [arg.lower() for arg in sys.argv[1:]]
    opciones_validas = ['piedra', 'papel', 'tijera']

    for jugada in listaH:
        if jugada not in opciones_validas:
            print(f'Error: {jugada} no es una jugada válida.')
            sys.exit(1)

    opciones = ['piedra', 'papel', 'tijera']
    listaM = [random.choice(opciones) for _ in range(3)]

    print('El usuario elige:', ' '.join(listaH))
    print('El programa elige:', ' '.join(listaM))

    resultado = jugar_partida(listaH, listaM)
    print('Ganador:', resultado)
