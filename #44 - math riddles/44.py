"""
Create an interactive terminal game in which you have to guess the result of different random mathematical operations (addition, subtraction, multiplication, or division of two integers).
- You will have 3 seconds to answer correctly.
- The game ends if you fail to respond within that time.
- Upon finishing the game, display the number of calculations you have guessed.
- Every 5 correct answers, increase by one the possible number of digits in the operation (each time in one operand):
  - Questions 1 to 5: X (between 0 and 9) operation Y (between 0 and 9)
  - Questions 6 to 10: XX (between 0 and 99) operation Y (between 0 and 9)
  - Questions 11 to 15: XX operation YY
  - Questions 16 to 20: XXX (between 0 and 999) operation YY
  ...
"""

import random
from pytimedinput import timedInput
import os

operators = ["+", "-", "*", "/"]
operations = []

result = 0
user_points = 0


def generate_question():
    global result
    global user_points

    operator = random.choice(operators)

    if user_points < 6:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif user_points < 11:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 9)
    elif user_points < 16:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
    else:
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        else:
            result = num1 / num2
    except ZeroDivisionError:
        result = 0

    if type(result) == float:
        generate_question()

    print(num1, operator, num2)
    ask_user(num1, operator, num2)


def ask_user(num1, operator, num2):
    global result
    global user_points

    answer = timedInput("= ", 3, False)

    try:
        if int(answer[0]) == result:
            user_points += 1
            generate_question()
    except ValueError:
        os.system('cls' if os.name == "nt" else "clear")
        print("Timed out.")
        print(f"Points: {user_points}")
        exit()


generate_question()
