# /*
#  * Este es un reto especial por Halloween.
#  * Te encuentras explorando una mansión abandonada llena de habitaciones.
#  * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#  * Tu misión es encontrar la habitación de los dulces.
#  *
#  * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
#  * (Tienes total libertad para ser creativo con los textos)
#  *
#  * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#  *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#  *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#  *   Esta podría ser una representación:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🍭⬜️
#  * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#  *   Si no lo aciertas no podrás desplazarte.
#  * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#  *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
#  * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
#  * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#  *   tengas que responder dos preguntas para salir de ella.
#  */



from preguntas import ENIGMAS
import random, copy
import unidecode

PREGUNTAS_HECHAS = []

def bienvenida():
    print("""
      ____  _                           _     _                 _          _                              _          _    _       _ _                              
 |  _ \(_)                         (_)   | |               | |        | |                            | |        | |  | |     | | |                             
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___       __ _| |        | |_   _  ___  __ _  ___     __| | ___    | |__| | __ _| | | _____      _____  ___ _ __  
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \     / _` | |    _   | | | | |/ _ \/ _` |/ _ \   / _` |/ _ \   |  __  |/ _` | | |/ _ \ \ /\ / / _ \/ _ \ '_ \ 
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |   | (_| | |   | |__| | |_| |  __/ (_| | (_) | | (_| |  __/   | |  | | (_| | | | (_) \ V  V /  __/  __/ | | |
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/     \__,_|_|    \____/ \__,_|\___|\__, |\___/   \__,_|\___|   |_|  |_|\__,_|_|_|\___/ \_/\_/ \___|\___|_| |_|
                                                                                     __/ |                                                                     
                                                                                    |___/                                                                   
    """)

def crearTablero():
    tablero=[]

    tablero = [[0,1,2,3] for _ in range(4)]
    posicion_puerta = posicionItems()
    posicion_dulce = posicionItems()

    if posicion_puerta == posicion_dulce:
        while posicion_puerta == posicion_dulce:
            posicion_dulce = posicionItems()

    return tablero, posicion_puerta, posicion_dulce

def fantasmas():
    numero = 0
    numero_random = random.randint(0, 9)

    if numero == numero_random:
        posicion = []
        posicion.append(random.randint(0,3))
        posicion.append(random.randint(0, 3))
        return posicion

def posicionItems():
    posicion = []
    posicion.append(random.randint(0, 3))
    if posicion[0] == 0 or posicion[0] == 3:
        posicion.append(random.randint(0, 3))
    else:
        posicion.append(random.choice([0, 3]))
    return posicion

def mover(movimiento, posicion):
    if movimiento == "norte" and posicion[0] - 1 >= 0:
        posicion[0] -= 1
        return posicion
    elif movimiento == "sur" and posicion[0] + 1 <= 4:
        posicion[0] += 1
        return posicion
    elif movimiento == "oeste" and posicion[1] -1 >= 0:
        posicion[1] -= 1
        return posicion
    elif movimiento == "este" and posicion[1] + 1 <= 4:
        posicion[1] += 1
        return posicion
    else:
        print("El movimiento no es válido")

def comprobarFantasma(lista1, lista2):
    fantasma = fantasmas()
    if fantasma != False:
        if fantasma == lista1 or fantasma == lista2:
            while fantasma == lista1 or fantasma == lista2:
                fantasma = fantasmas()
                comprobarFantasma(lista1, lista2)
        return fantasma

def generarEnigma():
    enigma = random.choice(ENIGMAS)
    pregunta = enigma['pregunta']
    if pregunta in PREGUNTAS_HECHAS:
        while pregunta in PREGUNTAS_HECHAS:
            enigma = random.choice(ENIGMAS)
            pregunta = enigma['pregunta']
    respuesta = enigma['respuesta']

    PREGUNTAS_HECHAS.append(pregunta)
    return pregunta, respuesta

contador = 0
def validarEnigma(esFantasma, pos_actual):
    global contador
    pregunta, respuesta = generarEnigma()
    respuesta_jugador = input(f"{pregunta}\n>>> ")

    respuesta = respuesta.lower().strip()
    respuesta = unidecode.unidecode(respuesta)
    respuesta_jugador = respuesta_jugador.lower().strip()
    respuesta_jugador = unidecode.unidecode(respuesta_jugador)

    if respuesta_jugador == respuesta:
        if esFantasma == True and contador < 1:
            print("¡Acertaste la Pregunta! Te queda una más para salir de esta habitación")
            contador += 1
            return True
        else:
            print("¡Acertaste la Pregunta! Conseguiste salir de esta habitación")
            crear_tablero[0][pos_actual[0]][pos_actual[1]] = completada
            dibujarTablero()
            contador = 0

    else:
        print("Respuesta incorrecta :( A la próxima será")
        return False

def dibujarTablero():
    calabaza = "🎃"
    print(calabaza*6)
    for elemento in crear_tablero[0]:
        print(' '.join(elemento))
    print(calabaza * 6)

crear_tablero = list(crearTablero())
tablero = copy.deepcopy(crear_tablero)
print(crear_tablero[0])
puerta = "🚪"
fantasma = "👻"
dulce_encontrado = "🍭"
dulce_no_encontrado = "⬜"
blanco = "⬜"
completada = "✔️"

n = 0
for elemento in crear_tablero[n]:
    for c in elemento:
        if type(c) == int:
            crear_tablero[0][n][c] = blanco
    n += 1

crear_tablero[0][crear_tablero[1][0]][crear_tablero[1][1]]=puerta
crear_tablero[0][crear_tablero[2][0]][crear_tablero[2][1]] = dulce_no_encontrado

bienvenida()
dibujarTablero()

posicion_inicial = crear_tablero[1]

while True:

    movimiento = input("¿Hacia que dirección quieres moverte?\n>>> ")
    posicion_actual = mover(movimiento, posicion_inicial)

    while posicion_actual == None or crear_tablero[0][posicion_actual[0]][posicion_actual[1]] == completada:
        movimiento = input("¿Hacia que dirección quieres moverte?\n>>> ")
        posicion_actual = mover(movimiento, posicion_inicial)

    fantasma1 = comprobarFantasma(crear_tablero[1], crear_tablero[2])
    fantasma2 = comprobarFantasma(crear_tablero[1], crear_tablero[2])
    while fantasma1 == fantasma2 and fantasma1 != None and fantasma2 != None:
        fantasma2 = comprobarFantasma(crear_tablero[1], crear_tablero[2])

    posicion_actual = [tablero[0][posicion_actual[0]][posicion_actual[0]], tablero[0][posicion_actual[0]][posicion_actual[1]]]
    if fantasma1 != None or fantasma2 != None:
        crear_tablero[0][posicion_actual[0]][posicion_actual[1]] = fantasma
        dibujarTablero()
        print("¡Te encontraste un Fantasma! Ahora tendrás que responder dos preguntas para salir de esta habitación.\n")
        for _ in range(2):
            true_or_false = validarEnigma(True, posicion_actual)
            if true_or_false == False:
                break

    elif posicion_actual == crear_tablero[2]:
        crear_tablero[0][posicion_actual[0]][posicion_actual[1]] = dulce_encontrado
        dibujarTablero()
        print("¡Encontraste el dulce! Se acabó el juego.")
        break

    else:
        print("Para pasar de habitación tendrás que responder la siguiente pregunta:\n")
        true_or_false = validarEnigma(False, posicion_actual)
        if true_or_false == False:
            break

