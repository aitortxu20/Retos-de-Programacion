"""
 * Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
"""

import random
from pytimedinput import timedInput
import os

operators = ["+", "-", "*", "/"]
operations = []

result = 0
user_points = 0


def generate_question():
    global result
    global user_points

    operator = random.choice(operators)

    if user_points < 6:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif user_points < 11:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 9)
    elif user_points < 16:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
    else:
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        else:
            result = num1 / num2
    except ZeroDivisionError:
        result = 0

    if type(result) == float:
        generate_question()

    print(num1, operator, num2)
    ask_user(num1, operator, num2)


def ask_user(num1, operator, num2):
    global result
    global user_points

    answer = timedInput("= ", 3, False)

    try:
        if int(answer[0]) == result:
            user_points += 1
            generate_question()
    except ValueError:
        os.system('cls' if os.name == "nt" else "clear")
        print("Timed out.")
        print(f"Points: {user_points}")
        exit()


generate_question()
