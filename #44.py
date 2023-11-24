# /*
#  * Crea un juego interactivo por terminal en el que tendrás que adivinar
#  * el resultado de diferentes
#  * operaciones matemáticas aleatorias (suma, resta, multiplicación
#  * o división de dos números enteros).
#  * - Tendrás 3 segundos para responder correctamente.
#  * - El juego finaliza si no se logra responder en ese tiempo.
#  * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
#  * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
#  *   de la operación (cada vez en un operando):
#  *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#  *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#  *   - Preguntas 11 a 15: XX operación YY
#  *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#  *   ...
#  */

import time
import random

puntuacion = 0
numx = 0
numy = 0
operaciones = ["mas", "menos", "por", "entre"]
jugar = "s"

def generar_numeros(puntuacion):

    if puntuacion < 6:
        numx = random.randint(0, 9)
        numy = random.randint(0, 9)
    elif puntuacion < 11:
        numx = random.randint(0, 99)
        numy = random.randint(0, 9)
    elif puntuacion < 16:
        numx = random.randint(0, 99)
        numy = random.randint(0, 99)
    else:
        numx = random.randint(0, 999)
        numy = random.randint(0, 99)

    return numx, numy

def llamar_operacion(operaciones, numx, numy):
    operacion = random.choice(operaciones)
    try:
        if operacion == "mas":
            resultado = numx + numy
            respuesta = int(input(f"Adivina cuanto es {numx} + {numy} >> "))
        elif operacion == "menos":
            resultado = numx - numy
            respuesta = int(input(f"Adivina cuanto es {numx} - {numy} >> "))
        elif operacion == "por":
            resultado = numx * numy
            respuesta = int(input(f"Adivina cuanto es {numx} * {numy} >> "))
        elif operacion == "entre":
            resultado = numx / numy
            respuesta = int(input(f"Adivina cuanto es {numx} / {numy} >> "))
        return resultado, respuesta
    except:
        llamar_operacion(operaciones, numx, numy)


print("Bienvenido al juego de operaciones matematicas")
while jugar == "s":
    numx, numy = generar_numeros(puntuacion)
    tiempo_actual = time.time()

    while True:

        if time.time() - tiempo_actual > 3:
            print("Respondiste pasaados 3 segundos, perdiste :(")
            break
        tiempo_actual = time.time()

        resultado, respuesta = llamar_operacion(operaciones, numx, numy)
        print(resultado, respuesta)
        if respuesta == resultado:
            puntuacion += 1
        #time.sleep(1)
        #tiempo -= 1

    jugar = input("Quieres volver a jugar? s/n: ").lower()

# Depurar esot del tiempo para que vaya



