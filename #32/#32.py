# /*
#  * Crea una función que calcule el número de la columna de una hoja de Excel
#  * teniendo en cuenta su nombre.
#  * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#  * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#  */

# SIN ACABAR
def n_columna(nombre):
    lista_alfabetica = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lista_alfabetica = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
contador=26
# for elemento in lista_alfabetica:
#     for elemento2 in lista_alfabetica:
#         contador+=1
#         celda=elemento+elemento2
#         if celda=="AC":
#             print(contador)

columna="AAA"
for elemento in range(len(columna)):
    valor=(lista_alfabetica.index(columna[elemento])+1)*26
    print(valor)







