# /*
#  * Crea una función que reciba dos parámetros para crear una cuenta atrás.
#  * - El primero, representa el número en el que comienza la cuenta.
#  * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#  * - Sólo se aceptan números enteros positivos.
#  * - El programa finaliza al llegar a cero.
#  * - Debes imprimir cada número de la cuenta atrás.
#  */

import time

def countdown(start, sleep):
    if start > 0:
        for i in range(start, -1, -1):
            print(i)
            time.sleep(sleep)
    else:
        print("Ey! Solo números enteros y POSITIVOS!!")

start = int(input("En que numero empieza?"))
sleep = int(input("Cuanto pasa entre cada cuenta?"))

countdown(start, sleep)