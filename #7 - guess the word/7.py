"""
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

import math
from random import randint, choice

words = ["degree", "inject", "battlefield", "deficit", "scan", "voucher"]
word = choice(words)
word_list = list(word)

replace_char = "_"

allowed_chars_to_replace = math.floor(len(word) * 0.6)

tries = 3

def generate_replace_word(replace_word):

    index = 0

    for i in word_list:
        
        while word_list.count(replace_char) < allowed_chars_to_replace:
            if randint(0, 1):
                word_list[index] = replace_char
            else:
                pass

            index += 1
            break
    
    return list(word_list)

def user_guess(guess_word):

    global tries

    while True:

        if guess_word == list(word):
            print("".join(guess_word))
            print("You guessed the word!")
            break

        print("".join(guess_word))
        print(f"You have {tries} more tries left")

        if tries == 0:
            break

        guess = input("Your guess: ")

        if guess == word:
            print("You guessed the word!")
            break

        index = 0

        for i in word:
            if word[index] != guess_word[index]:
                if guess == word[index]:
                    guess_word[index] = i
                    if tries <= 3:
                        tries += 1
            else:
                pass
            
            index += 1
        tries -= 1
            

user_guess(generate_replace_word(word_list))
