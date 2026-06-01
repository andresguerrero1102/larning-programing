import random

jugadores = 0
meta = 0
posiciones = []
dobles = []
ganador = False


def pedir_jugadores():
    jugadores = int(input("Cantidad de jugadores (2 a 4): "))

    while jugadores < 2 or jugadores > 4:
        jugadores = int(input("Ingrese entre 2 y 4 jugadores: "))

    return jugadores


def pedir_meta():
    print("\n1. 20 posiciones")
    print("2. 30 posiciones")
    print("3. 50 posiciones")
    print("4. 100 posiciones")

    opcion = int(input("Seleccione nivel: "))

    if opcion == 1:
        return 20
    elif opcion == 2:
        return 30
    elif opcion == 3:
        return 50
    else:
        return 100


def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


def jugar():
    jugadores = pedir_jugadores()
    meta = pedir_meta()

    posiciones = [0] * jugadores
    dobles = [0] * jugadores

    ganador = False

    while ganador == False:

        for i in range(jugadores):

            print("\nTurno Jugador", i + 1)

            dado1, dado2 = lanzar_dados()

            print("Dado 1:", dado1)
            print("Dado 2:", dado2)

            if dado1 == dado2:
                dobles[i] += 1
            else:
                dobles[i] = 0

            if dobles[i] == 3:
                print("¡Jugador", i + 1, "gana por 3 dobles!")
                ganador = True
                break

            avance = dado1 + dado2
            posiciones[i] += avance

            print("Posición:", posiciones[i])

            if posiciones[i] >= meta:
                print("¡Jugador", i + 1, "llegó a la meta!")
                ganador = True
                break


jugar()
