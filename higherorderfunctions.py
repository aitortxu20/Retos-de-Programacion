# def funcion_a(funcion_b):
#     def funcion_c(a,b):
#         print('Antes de la ejecución de la función a decorar')
#         a=10
#         b=20
#         result = funcion_b(a,b)
#         print(result)
#         print('Después de la ejecución de la función a decorar')
#
#         return result
#
# #     return funcion_c
#
# @funcion_a
# def suma(a, b):
#     return a + b
#
# suma(7,5)
from functools import reduce

diccionarioRomano = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,"IX": 9, "V": 5, "IV": 4, "I": 1}

def convertir(numero):
    diccionarioRomano = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
                         "IX": 9, "V": 5, "IV": 4, "I": 1}


    entero = 0
    resto = 0
    numeroromano = ""

    for k, v in diccionarioRomano.items():
        entero = numero // v
        resto = numero % v
        numeroromano += k * entero
        numero = resto

    return numeroromano


def romano_a_entero(string):
    diccionarioRomano = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
                         "IX": 9, "V": 5, "IV": 4, "I": 1}

    listavalores = []
    for elemento in string:
        listavalores.append(diccionarioRomano[elemento])


    for i in range(0, len(listavalores)-1):
        if listavalores[i] < listavalores[i+1]:
            listavalores[i] *= -1

    resultado = reduce((lambda a,b: a+b), listavalores)
    print(resultado)
print(convertir(1498))
romano_a_entero(convertir(1498))