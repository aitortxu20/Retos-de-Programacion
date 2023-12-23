"""
Create a program that simulates a competition between two cars on a track.
- Both cars will be represented by 🚙 and 🚗. The finish line will be represented by 🏁.
- Each track will have between 1 and 3 trees 🌲 randomly placed.
- Both tracks will have a configurable length of underscores "_".
- The cars will start on the right side of the tracks. Example:
    🏁____🌲_____🚙
    🏁_🌲____🌲___🚗

The game unfolds automatically in turns, and every second an action is taken on the cars (moving at the same time), until one of them (or both) reaches the finish line.
- Actions:
  - Move between 1 to 3 positions towards the finish line.
  - If, while moving, the car ends up in the position of a tree,
    display 💥 and do not advance for one turn.
  - Each turn prints the tracks and their elements.
  - When the race finishes, display the winning car or the tie.
"""

import random
import time
import os


class Car:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.turn = True

    def move(self, movement_units):
        self.position -= movement_units


class Track:
    def __init__(self, track_size):
        self.finish_line = 0
        self.track_size = track_size
        self.trees = []
        self.num_trees = random.randint(1, 3)
        for element in range(self.num_trees):
            self.trees.append(random.randint(1, self.track_size - 2))

    def print_track(self, car):
        self.track = "🏁"

        for i in range(1, self.track_size):
            if i not in self.trees and i != car.position:
                self.track += '_'
            elif i == car.position:
                self.track += car.color
            else:
                self.track += "🌲"

        if car.position == self.track_size:
            self.track += car.color
        if car.position == 0:
            self.track = car.color + self.track[1:]

        if car.position in self.trees:
            self.track = self.track[0:car.position - 1] + "💥" + self.track[car.position + 1:]
            car.turn = False
            self.trees.remove(car.position)
            print(self.track)
        else:
            print(self.track)


def check_winner(blue_car_pos: int, red_car_pos: int):
    if red_car_pos == 0 and blue_car_pos == 0:
        print("It's a tie!")
    elif red_car_pos <= 0:
        print(f"{car_red.color} car won!")
    elif blue_car_pos <= 0:
        print(f"{car_blue.color} car won!")


track_size = int(input("What should be the track size: "))
car_red = Car(track_size, "🚗")
car_blue = Car(track_size, "🚙")
track_red = Track(track_size)
track_blue = Track(track_size)
track_red.print_track(car_red)
track_blue.print_track(car_blue)

while car_red.position > 0 and car_blue.position > 0:
    time.sleep(0.5)
    if car_red.turn == True:
        car_red.move(random.randint(1, 3))
    else:
        car_red.move(0)
        car_red.turn = True

    if car_blue.turn == True:
        car_blue.move(random.randint(1, 3))
    else:
        car_blue.move(0)
        car_blue.turn = True

    os.system("clear")
    track_red.print_track(car_red)
    track_blue.print_track(car_blue)
    check_winner(car_blue.position, car_red.position)
