# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  */


def triplesPitagoricos(numero):
    numeroc = numero ** 2
    listaResultados = []
    for n in range(1, numero-1):
        print("intento " ,n)
        for n2 in range(1, numero-1):
            if n**2 + n2**2 == numeroc:
                tupla = (n, n2, numeroc)
                listaResultados.append(tupla)
    return listaResultados

resultado = triplesPitagoricos(int(input("Introduce un número ")))

print(resultado)

