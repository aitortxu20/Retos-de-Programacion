"""
Create a small game that involves guessing words within a maximum number of attempts:

- The game starts by proposing a randomly incomplete word, for example, "m_ur_d_v," along with the remaining number of attempts.
- The user can only input a single letter or a word (of the same length as the word to be guessed).
  - If the user inputs a letter and guesses correctly, that letter is revealed in the word. If they guess incorrectly, one attempt is deducted.
  - If the user inputs a complete guess and is correct, the game ends. Otherwise, one attempt is deducted.
  - If the attempt counter reaches 0, the player loses.
- The word should randomly hide letters, and it should not start by hiding more than 60% of the letters.
- You can use any words and choose the number of attempts you deem appropriate.
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
