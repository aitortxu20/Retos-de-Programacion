"""
This is a special Halloween challenge.
You find yourself exploring an abandoned mansion full of rooms.
In each room, you'll have to solve a riddle to progress to the next one.
Your mission is to find the candy room.
The task is to implement an interactive question-and-answer game via the terminal.
(You have complete freedom to be creative with the texts)
🏰 House: The mansion corresponds to a 4 x 4 square structure that you'll need to model. Rooms with doors and candy rooms do not have riddles.
(16 rooms, with one entrance and one containing the candy)

Here could be a representation:

🚪⬜️⬜️⬜️
⬜️👻⬜️⬜️
⬜️⬜️⬜️👻
⬜️⬜️🍭⬜️

❓ Riddles: Each room presents a random riddle that you must answer with text.
If you don't guess it, you won't be able to move.
🧭 Movement: If you solve the riddle, you'll be asked where you want to move.
(Example: north/south/east/west. Only the possible options should be provided)
🍭 Exit: You exit the house if you find the candy room.
👻 (Bonus) Ghosts: There is a 10% chance that a ghost appears in a room, and you have to answer two questions to leave it.
"""

import random
import os
import sys

BOARD_ROWS = 4
BOARD_COLUMNS = 4
EMPTY_CELL = "⬜️"
DOOR_CELL = "🚪"
GHOST_CELL = "👻"
CANDY_CELL = "🍭"
QUESTION_CELL = "❓"
CHECK_CELL = "✅"

cellsPositions = []
firstMove = False

askedQuestions = []

board = [[EMPTY_CELL] * BOARD_COLUMNS for _ in range(BOARD_ROWS)]


def showBoard(board):
    if firstMove == True:
        clearScreen()
    for row in board:
        print("".join(row))


def clearScreen():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    else:
        pass


def generatePosition(selectedCell):
    cellPosition = [random.randrange(
        BOARD_ROWS), random.randrange(BOARD_COLUMNS)]

    if cellPosition not in cellsPositions:
        cellsPositions.append(cellPosition)
    else:
        generatePosition(selectedCell)

    return cellPosition


def replaceRandoms():
    global doorPosition, candyPosition

    doorPosition = None
    candyPosition = None

    while doorPosition == candyPosition:
        doorPosition = generatePosition(DOOR_CELL)
        candyPosition = generatePosition(CANDY_CELL)

    board[doorPosition[0]][doorPosition[1]] = DOOR_CELL


def playerPosition():
    global currentPosition, possibleMoves

    if firstMove == False:
        currentPosition = doorPosition
        possibleMoves = None

    if currentPosition[0] == 0:

        if currentPosition[1] == 0:
            possibleMoves = "[R]ight, [D]own"
        elif currentPosition[1] == BOARD_COLUMNS - 1:
            possibleMoves = "[L]eft, [D]own"
        else:
            possibleMoves = "[L]eft, [R]ight, [D]own"

    elif currentPosition[0] == BOARD_ROWS - 1:

        if currentPosition[1] == 0:
            possibleMoves = "[R]ight, [U]p"
        elif currentPosition[1] == BOARD_COLUMNS - 1:
            possibleMoves = "[L]eft, [U]p"
        else:
            possibleMoves = "[L]eft, [R]ight, [U]p"

    else:

        if currentPosition[1] == 0:
            possibleMoves = "[R]ight, [U]p, [D]own"
        elif currentPosition[1] == BOARD_COLUMNS - 1:
            possibleMoves = "[L]eft, [U]p, [D]own"
        else:
            possibleMoves = "[L]eft, [R]ight, [U]p, [D]own"


def playerMove():
    global firstMove

    playerPosition()

    playerMove = input(f"Where to move {possibleMoves} > ")
    firstMove = True

    if playerMove == "L":
        currentPosition[1] -= 1
    elif playerMove == "R":
        currentPosition[1] += 1
    elif playerMove == "U":
        currentPosition[0] -= 1
    elif playerMove == "D":
        currentPosition[0] += 1

    replaceCell()


def askQuestion():
    haloweenQuestions = [
        {"q": "When is Halloween?", "a": "October 31"},
        {"q": "Traditional Halloween carving?", "a": "Pumpkins"},
        {"q": "What's said when trick-or-treating?", "a": "Trick or treat"},
        {"q": "Belief about black cats?", "a": "Brings bad luck"},
        {"q": "Fear of Halloween is called?", "a": "Samhainophobia"},
        {"q": "Who is the author of 'The Legend of Sleepy Hollow'?",
            "a": "Washington Irving"},
        {"q": "Purpose of a scarecrow?", "a": "Keep away evil spirits"},
        {"q": "Traditional apple bobbing?", "a": "Biting apples in water"},
        {"q": "The name of a ghost in 'A Christmas Carol'?", "a": "Jacob Marley"},
        {"q": "'Witch' in Old English?", "a": "Wicce"},
        {"q": "One popular Halloween candy?", "a": "Snickers"},
        {"q": "Michael Myers movie?", "a": "Halloween 1978"},
        {"q": "Mexican name for Halloween?", "a": "Dia de los Muertos"},
        {"q": "Common Halloween costume?",
            "a": "Superheroes"},
        {"q": "What means breaking a mirror superstition?",
            "a": "Seven years of bad luck"}
    ]

    chosenQuestion = random.choice(haloweenQuestions)

    while chosenQuestion in askedQuestions:
        chosenQuestion = random.choice(haloweenQuestions)
    askedQuestions.append(chosenQuestion)

    print(f"🎃 Riddle time 🎃\n{chosenQuestion['q']}")

    playerAnswer = ""
    while playerAnswer.lower() != chosenQuestion["a"].lower():
        playerAnswer = input("> ")

        if playerAnswer.lower() == chosenQuestion["a"].lower():

            if ghostFound == True:
                if ghostAsked > 1:
                    board[currentPosition[0]][currentPosition[1]] = CHECK_CELL
                    showBoard(board)
                    playerMove()
            else:
                board[currentPosition[0]][currentPosition[1]] = CHECK_CELL
                showBoard(board)
                playerMove()

        else:
            print("❌ Wrong answer! Try again..")


def replaceCell():
    global ghostFound, ghostAsked

    ghostFound = False
    ghostAsked = 0

    if random.randrange(10) == 0:

        if currentPosition != candyPosition and board[currentPosition[0]][currentPosition[1]] != CHECK_CELL:

            board[currentPosition[0]][currentPosition[1]] = GHOST_CELL
            showBoard(board)
            print("👻 You found a ghost. Answer two questions to move.")
            ghostFound = True

            for _ in range(2):
                ghostAsked += 1
                askQuestion()

    if currentPosition == candyPosition:
        board[currentPosition[0]][currentPosition[1]] = CANDY_CELL
        showBoard(board)
        print("🎉 You found the candy! Congratulations!")
        exit()

    elif board[currentPosition[0]][currentPosition[1]] == EMPTY_CELL:

        board[currentPosition[0]][currentPosition[1]] = QUESTION_CELL
        showBoard(board)
        askQuestion()

    elif board[currentPosition[0]][currentPosition[1]] == CHECK_CELL:

        print("You already answered the question in this cell! Move to another! 🔄")
        showBoard(board)
        playerMove()


print("""
🎃 Welcome to the Halloween Mansion Adventure! 🏰

🔍 Answer riddles to move through rooms. Beware of ghosts! They might have questions too! 👻

🎉 Your goal: Find the candy room 🍭 and celebrate your Halloween victory! Good luck! 🕸️🕷️
""")
replaceRandoms()
showBoard(board)
playerMove()
