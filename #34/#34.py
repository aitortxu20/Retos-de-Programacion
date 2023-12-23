# /*
#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
#  * Únicamente el código.
#  *
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero.
#  */

try:
    with open("text.txt", "r") as f:

            contenido = f.readlines()
            print(contenido)
            opcion = input("El fichero existe. Quieres seguir escribiendo? S/N: ")
            if opcion == "S":

                with open("text.txt", "a") as f:

                    texto = input("Introduce un texto append: ")
                    f.write(texto)
                    f.write("\n")

            else:
                with open("text.txt", "w") as f:
                    texto = input("Introduce un texto write: ")
                    f.write(texto)
                    f.write("\n")
except:
    with open("text.txt", "w") as f:
        texto = input("Introduce un texto excepcion: ")
        f.write(texto)

