"""
Create a function that takes two parameters to set up a countdown.
- The first parameter represents the number from which the countdown begins.
- The second parameter represents the seconds that should elapse between each count.
- Only positive integers are accepted.
- The program terminates when it reaches zero.
- You should print each number in the countdown.
"""

from time import sleep


def cooldown(start_number, wait_time):

    if type(start_number) == int and start_number > 0:

        for i in range(start_number):
            print(start_number)
            sleep(wait_time)
            start_number -= 1

        print(0)


cooldown(10, 2)
