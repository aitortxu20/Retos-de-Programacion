"""
* Create a program that simulates a competition between two cars on a track.
* - The two cars will be represented by 🚙 and 🚗. And the finish line by 🏁.
* - Each track will have between 1 and 3 trees 🌲 placed randomly.
* - Both tracks will have a configurable length of underscores "_".
* - The cars will start on the right side of the tracks. Example:
*   🏁____🌲_____🚙
*   🏁_🌲____🌲___🚗
* 
* The game progresses automatically in turns, and every second
* an action is taken on the cars (moving simultaneously) until
* one of them (or both) reaches the finish line.
* - Actions:
*   - Move forward 1 to 3 positions towards the finish line.
*   - If, while advancing, the car ends up in the position of a tree,
*     display 💥 and do not move for one turn.
*   - Each turn, print the tracks and their elements.
*   - When the race ends, display the winning car or declare a tie.
"""

import random
from time import sleep
import os
import sys

TRACKLENGTH = 10
TURN_DURATION = 1


class Track():
    def __init__(self, track_length, car):

        self.car = car
        self.track = ["_"] * track_length
        self.track.append(self.car.color)
        self.track.insert(0, "🏁")
        self.addTrees()

    def showTrack(self):
        print("".join(self.track))

    def addTrees(self):
        self.trees = generateTrees()

        for treePosition in self.trees:
            self.track[treePosition] = "🌲"

    def replaceCells(self):
        carPosition = self.car.getPosition(self)
        randomMove = self.car.moveCar()

        self.track[carPosition] = "_"
        newCarPosition = self.track[carPosition - randomMove]

        if newCarPosition == "🌲":
            self.track[carPosition - randomMove] = "💥"
        else:
            self.track[carPosition - randomMove] = self.car.color

        self.checkTrackEnd()

    def checkTrackEnd(self):

        if "🏁" not in self.track:
            compareTracks()


class Car():
    def __init__(self, color):
        self.color = color

    def getPosition(self, track):
        self.track = track

        if "💥" not in self.track.track:
            carPosition = self.track.track.index(self.color)
        else:
            carPosition = self.track.track.index("💥")

        return carPosition

    def moveCar(self):
        carPosition = self.getPosition(self.track)

        if self.color not in self.track.track:
            randomMove = 0
        else:
            if carPosition == 1:
                randomMove = 1
            elif carPosition == 2:
                randomMove = random.randint(1, 2)
            else:
                randomMove = random.randint(1, 3)

        return randomMove


def showTracks():
    blueCarTrack.showTrack()
    redCarTrack.showTrack()


def clearScreen():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    else:
        pass


def generateTrees():
    howManyTrees = random.randint(1, 3)
    trees = []

    for _ in range(howManyTrees):

        treePosition = random.randint(1, TRACKLENGTH)

        while treePosition in trees:
            treePosition = random.randint(1, TRACKLENGTH)

        trees.append(treePosition)

    return trees


blueCarTrack = Track(TRACKLENGTH, Car("🚙"))
redCarTrack = Track(TRACKLENGTH, Car("🚗"))


def startRace():

    showTracks()

    sleep(TURN_DURATION)
    clearScreen()

    while True:

        blueCarTrack.replaceCells()
        redCarTrack.replaceCells()

        showTracks()

        sleep(TURN_DURATION)
        clearScreen()


def compareTracks():
    showTracks()

    if blueCarTrack.track[0] == "🏁":
        print(f"{redCarTrack.car.color} WINS")
    elif redCarTrack.track[0] == "🏁":
        print(f"{blueCarTrack.car.color} WINS")
    else:
        print(f"DRAW")

    exit()


startRace()
