"""
Write a program that displays on the console (using print) the numbers from 1 to 100 (both included, with a newline between each print), replacing the following:
- Multiples of 3 with the word "fizz."
- Multiples of 5 with the word "buzz."
- Multiples of both 3 and 5 with the word "fizzbuzz."
"""

for n in range(100):
    n += 1

    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)

    print("\n")
