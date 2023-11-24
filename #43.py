# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */

import random

def clima(dias, temperatura, probabilidad):
    lista_valores = []
    n = 0
    n_random = random.randrange(0,10)
    variacion = random.choice((0, 1))
    dias_de_lluvia = 0


    for i in range(1, dias+1):
        if n == n_random:
            if variacion == 0:
                temperatura += 2
            else:
                temperatura -= 2
        if temperatura > 25 and probabilidad <= 80:
            probabilidad += 20
        elif temperatura > 25:
            probabilidad = 100

        if temperatura < 5 and probabilidad >= 20:
            probabilidad -= 20
        elif temperatura < 5:
            probabilidad = 0


        if probabilidad == 100:
            temperatura -= 1
            dias_de_lluvia += 1



        lista_valores.append((temperatura,probabilidad))
        print(f"Dia numero {i}, tempreratura {temperatura} y una probabilidad de lluvia de {probabilidad}%")
    print(lista_valores)
    maximo = lista_valores[0][0]
    minimo = lista_valores[0][0]
    for max, prob in lista_valores:
        if max > maximo:
            maximo = max
        if max < minimo:
            minimo = max

    print(f"La temperatura maximo ha sido {maximo}, la minima ha sido {minimo} ha llovido {dias_de_lluvia} dias")




clima(5, -7, 60)





