"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

import string

alphabet = list(string.ascii_lowercase)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

leet_alphabet = ["4", "I3", "[", ")", "3", "|=",
                 "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\/", "\/\/", "><", "j", "2"]
leet_numbers = ["o", "L", "R", "E", "A", "S", "b", "T", "B", "g"]

text = input("Type a text > ")


def text_to_leet():

    print("\nText --> Leet\n")

    leet_text = ""

    for character in text:

        if character in alphabet:
            index = alphabet.index(character.lower())
            character = leet_alphabet[index]
            leet_text += character
        else:
            try:
                character = int(character)
                index = numbers.index(character)
                character = leet_numbers[index]
                leet_text += character
            except:
                leet_text += character

    return leet_text


print(text_to_leet())
