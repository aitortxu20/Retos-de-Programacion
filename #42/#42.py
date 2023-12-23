# /*
#  * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
#  * en dos dimensiones.
#  * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
#  *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
#  * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
#  * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
#  * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.
#  */

# d = √((x2 - x1)² + (y2 - y1)²)

import math
from sympy import symbols, Eq, solve

punto_a = [0, 0]
velocidad_a = [2, 2]
puntob = [3, 3]
velocidadb = [-2, -2]

t = symbols('t')
eq_x = Eq(punto_a[0] + velocidad_a[0] * t, puntob[0] + velocidadb[0] * t)
eq_y = Eq(punto_a[1] + velocidad_a[1] * t, puntob[1] + velocidadb[1] * t)

sol = solve((eq_x, eq_y), (t))

if sol:
    tiempo_interseccion = sol[t]
    posicion_interseccion = (punto_a[0] + velocidad_a[0] * tiempo_interseccion,
                             punto_a[1] + velocidad_a[1] * tiempo_interseccion)
    print("Tiempo de intersección:", tiempo_interseccion)
    print("Posición de intersección:", posicion_interseccion)
else:
    print("Los vectores no se intersectan.")

def colision(a, speed_a, b, speed_b):
    distancia = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    distancia2 = distancia
    pos_nueva_a = [a[0], a[1]]
    pos_nueva_b = [b[0], b[1]]
    tiempo = 0

    while distancia2 > 0 and distancia2 <= distancia:
        pos_nueva_a[0] = (pos_nueva_a[0] + speed_a[0])
        pos_nueva_a[1] = (pos_nueva_a[1] + speed_a[1])
        pos_nueva_b[0] = (pos_nueva_b[0] + speed_b[0])
        pos_nueva_b[1] = (pos_nueva_b[1] + speed_b[1])
        tiempo += 1

        distancia2 = math.sqrt((pos_nueva_a[0] - pos_nueva_b[0])**2 + (pos_nueva_a[1] - pos_nueva_b[1])**2)

        if distancia2 == 0.0:
            print(f"Han colisionado en ({pos_nueva_a[0]}, {pos_nueva_a[1]}) y han tardado {tiempo} unidades de tiempo")
        elif distancia2 > distancia:
            print("Los objetos no se van a chochar nunca")
            print(tiempo-1)
            break
        elif distancia2 == distancia:
            print("Los objetos se mueven de forma paralela")
            break


colision(punto_a, velocidad_a, puntob, velocidadb)