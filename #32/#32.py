# /*
#  * Crea una función que calcule el número de la columna de una hoja de Excel
#  * teniendo en cuenta su nombre.
#  * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#  * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#  */

def columna_excel_a_numero(columna):
    letras = {chr(i): i - 64 for i in range(65, 91)}
    resultado = 0

    for i in range(len(columna)):
        letra = columna[len(columna) - 1 - i]
        resultado += letras[letra] * (26 ** i)

    return resultado

print(columna_excel_a_numero("A"))
print(columna_excel_a_numero("Z"))
print(columna_excel_a_numero("AA"))
print(columna_excel_a_numero("BFP"))

