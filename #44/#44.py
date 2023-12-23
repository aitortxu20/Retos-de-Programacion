# Create an interactive terminal game where you'll need to guess
# the result of different random mathematical operations (addition, subtraction,
# multiplication, or division of two integers).
# - You'll have 3 seconds to answer correctly.
# - The game ends if the correct answer isn't provided within that time.
# - At the end of the game, display how many calculations you've guessed correctly.
# - For every 5 correct answers, increase the potential number of digits
#   in the operation (each time in one operand):
#   - Questions 1 to 5: X (between 0 and 9) operation Y (between 0 and 9)
#   - Questions 6 to 10: XX (between 0 and 99) operation Y (between 0 and 9)
#   - Questions 11 to 15: XX operation YY
#   - Questions 16 to 20: XXX (between 0 and 999) operation YY

import time
import random

score = 0
digits = [1, 2]
operators = ["+", "-", "*", "/"]

print("Welcome to the Math Game!")


def generate_numbers(score):
    if score < 5:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif score < 10:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 9)
    elif score < 15:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
    else:
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)

    return num1, num2


def perform_operation(num1, num2, operator):
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        return result
    except ZeroDivisionError:
        return None


while True:
    num1, num2 = generate_numbers(score)
    operator = random.choice(operators)
    correct_answer = perform_operation(num1, num2, operator)
    print(f"What is {num1} {operator} {num2}?")

    start_time = time.time()
    user_answer = input("Your answer: ")
    end_time = time.time()

    if end_time - start_time > 3:
        print("Time's up!")
        break

    try:
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Game over! You got {score} calculations correct.")



