"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
"""

from time import sleep


def cooldown(start_number, wait_time):

    if type(start_number) == int and start_number > 0:

        for i in range(start_number):
            print(start_number)
            sleep(wait_time)
            start_number -= 1

        print(0)


cooldown(10, 2)
