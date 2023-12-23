# /*
#  * Crea un programa que simule la competición de dos coches en una pista.
#  * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
#  * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
#  * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
#  * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
#  *   🏁____🌲_____🚙
#  *   🏁_🌲____🌲___🚗
#  *
#  * El juego se desarrolla por turnos de forma automática, y cada segundo
#  * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
#  * uno de ellos (o los dos a la vez) llega a la meta.
#  * - Acciones:
#  *   - Avanzar entre 1 a 3 posiciones hacia la meta.
#  *   - Si al avanzar, el coche finaliza en la posición de un árbol,
#  *     se muestra 💥 y no avanza durante un turno.
#  *   - Cada turno se imprimen las pistas y sus elementos.
#  *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
#  *
#  */

import random
import time
import os

class Coche:
    def __init__(self, posicion, color):
        self.posicion = posicion
        self.color = color
        self.turno = True
    def mover(self, unidades_movimiento):
        self.posicion -= unidades_movimiento

class Pista:
    def __init__(self, tamano_pista):
        self.meta = 0
        self.tamano_pista = tamano_pista
        self.arboles = []
        self.num_arboles = random.randint(1, 3)
        for elemento in range(self.num_arboles):
            self.arboles.append(random.randint(1, self.tamano_pista - 2))

    def imprimir_pista(self, coche):
        self.pista = "🏁"

        for i in range(1, self.tamano_pista):
            if i not in self.arboles and i != coche.posicion:
                self.pista += '_'
            elif i == coche.posicion:
                self.pista += coche.color
            else:
                self.pista += "🌲"

        if coche.posicion == tamano_pista:
            self.pista += coche.color
        if coche.posicion == 0:
            self.pista = coche.color + self.pista[1:]

        if coche.posicion in self.arboles:
            self.pista = self.pista[0:coche.posicion - 1] + "💥" + self.pista[coche.posicion + 1:]
            coche.turno = False
            self.arboles.remove(coche.posicion)
            print(self.pista)
        else:
            print(self.pista)

def check_ganador(coche_azul_pos: int, coche_rojo_pos: int):
    if coche_rojo_pos == 0 and coche_azul_pos == 0:
        print("Empate!")
    elif coche_rojo_pos <= 0:
        print(f"Ganó el {coche_rojo.color}")
    elif coche_azul_pos <= 0:
        print(f"Ganó el {coche_azul.color}")

tamano_pista = int(input("Cual quieres que sea el tamaño de la pista: "))
coche_rojo = Coche(tamano_pista, "🚗")
coche_azul = Coche(tamano_pista, "🚙")
pista_rojo = Pista(tamano_pista)
pista_azul = Pista(tamano_pista)
pista_rojo.imprimir_pista(coche_rojo)
pista_azul.imprimir_pista(coche_azul)

while coche_rojo.posicion > 0 and coche_azul.posicion > 0:
    time.sleep(0.5)
    if coche_rojo.turno == True:
        coche_rojo.mover(random.randint(1, 3))
    else:
        coche_rojo.mover(0)
        coche_rojo.turno = True

    if coche_azul.turno == True:
        coche_azul.mover(random.randint(1, 3))
    else:
        coche_azul.mover(0)
        coche_azul.turno = True

    os.system("clear")
    pista_rojo.imprimir_pista(coche_rojo)
    pista_azul.imprimir_pista(coche_azul)
    check_ganador(coche_azul.posicion, coche_rojo.posicion)