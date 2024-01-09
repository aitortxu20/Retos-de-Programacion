"""
Write a program that takes input text and transforms natural language into "hacker language" (commonly known as "leet" or "1337"). This language is characterized by substituting alphanumeric characters.
- Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) with the alphabet and numbers in "leet."
  (Use the first option for each transformation. For example, "4" for "a.")
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
        else:
            try:
                character = int(character)
                index = numbers.index(character)
                character = leet_numbers[index]
            except:
                pass

        leet_text += character

    return leet_text


print(text_to_leet())
