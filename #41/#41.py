# /*
#  * This is a special challenge for Halloween.
#  * You find yourself exploring an abandoned mansion full of rooms.
#  * In each room, you'll have to solve a riddle to advance to the next one.
#  * Your mission is to find the candy room.
#  *
#  * This involves implementing an interactive question-and-answer game via the terminal.
#  * (You have total freedom to be creative with the texts)
#  *
#  * - 🏰 House: The mansion corresponds to a 4 x 4 square structure
#  *   that you should model. Rooms with a door and candy do not have a riddle.
#  *   (16 rooms, one for entry and one where the candy is located)
#  *   This could be a representation:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🍭⬜️
#  * - ❓ Riddles: Each room presents a random riddle that you must answer with text.
#  *   If you don't solve it, you can't move.
#  * - 🧭 Movement: If you solve the riddle, you'll be asked where you want to move.
#  *   (Example: north/south/east/west. Only possible options should be provided)
#  * - 🍭 Exit: You leave the house if you find the candy room.
#  * - 👻 (Bonus) Ghosts: There's a 10% chance that a ghost appears in a room and
#  *   you have to answer two questions to leave.
#  */

from preguntas import ENIGMAS
import random, copy
import unidecode

ASKED_QUESTIONS = []

def welcome():
    print("""
      ____  _                           _     _                 _          _                              _          _    _       _ _                              
 |  _ \(_)                         (_)   | |               | |        | |                            | |        | |  | |     | | |                             
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___       __ _| |        | |_   _  ___  __ _  ___     __| | ___    | |__| | __ _| | | _____      _____  ___ _ __  
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \     / _` | |    _   | | | | |/ _ \/ _` |/ _ \   / _` |/ _ \   |  __  |/ _` | | |/ _ \ \ /\ / / _ \/ _ \ '_ \ 
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |   | (_| | |   | |__| | |_| |  __/ (_| | (_) | | (_| |  __/   | |  | | (_| | | | (_) \ V  V /  __/  __/ | | |
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/     \__,_|_|    \____/ \__,_|\___|\__, |\___/   \__,_|\___|   |_|  |_|\__,_|_|_|\___/ \_/\_/ \___|\___|_| |_|
                                                                                     __/ |                                                                     
                                                                                    |___/                                                                   
    """)

def createBoard():
    board=[]

    board = [[0,1,2,3] for _ in range(4)]
    door_position = getPositions()
    candy_position = getPositions()

    if door_position == candy_position:
        while door_position == candy_position:
            candy_position = getPositions()

    return board, door_position, candy_position

def ghosts():
    number = 0
    random_number = random.randint(0, 9)

    if number == random_number:
        position = []
        position.append(random.randint(0,3))
        position.append(random.randint(0, 3))
        return position

def getPositions():
    position = []
    position.append(random.randint(0, 3))
    if position[0] == 0 or position[0] == 3:
        position.append(random.randint(0, 3))
    else:
        position.append(random.choice([0, 3]))
    return position

def move(direction, position):
    if direction == "north" and position[0] - 1 >= 0:
        position[0] -= 1
        return position
    elif direction == "south" and position[0] + 1 <= 4:
        position[0] += 1
        return position
    elif direction == "west" and position[1] -1 >= 0:
        position[1] -= 1
        return position
    elif direction == "east" and position[1] + 1 <= 4:
        position[1] += 1
        return position
    else:
        print("Invalid movement")

def checkGhost(list1, list2):
    ghost = ghosts()
    if ghost != False:
        if ghost == list1 or ghost == list2:
            while ghost == list1 or ghost == list2:
                ghost = ghosts()
                checkGhost(list1, list2)
        return ghost

def generateRiddle():
    riddle = random.choice(ENIGMAS)
    question = riddle['pregunta']
    if question in ASKED_QUESTIONS:
        while question in ASKED_QUESTIONS:
            riddle = random.choice(ENIGMAS)
            question = riddle['pregunta']
    answer = riddle['respuesta']

    ASKED_QUESTIONS.append(question)
    return question, answer

counter = 0
def validateRiddle(isGhost, current_position):
    global counter
    question, answer = generateRiddle()
    player_answer = input(f"{question}\n>>> ")

    answer = answer.lower().strip()
    answer = unidecode.unidecode(answer)
    player_answer = player_answer.lower().strip()
    player_answer = unidecode.unidecode(player_answer)

    if player_answer == answer:
        if isGhost == True and counter < 1:
            print("You got the first question right! You have one more to leave this room")
            counter += 1
            return True
        else:
            print("You got the question right! You managed to leave this room")
            createBoard[0][current_position[0]][current_position[1]] = completed
            drawBoard()
            counter = 0

    else:
        print("Incorrect answer :( Better luck next time")
        return False

def drawBoard():
    pumpkin = "🎃"
    print(pumpkin*6)
    for element in createBoard[0]:
        print(' '.join(element))
    print(pumpkin * 6)

createBoard = list(createBoard())
board = copy.deepcopy(createBoard)
print(createBoard[0])
door = "🚪"
ghost = "👻"
found_candy = "🍭"
not_found_candy = "⬜"
blank = "⬜"
completed = "✔️"

n = 0
for element in createBoard[n]:
    for c in element:
        if type(c) == int:
            createBoard[0][n][c] = blank
    n += 1

createBoard[0][createBoard[1][0]][createBoard[1][1]] = door
createBoard[0][createBoard[2][0]][createBoard[2][1]] = not_found_candy

welcome()
drawBoard()

initial_position = createBoard[1]

while True:

    movement = input("Which direction do you want to move?\n>>> ")
    current_position = move(movement, initial_position)

    while current_position == None or createBoard[0][current_position[0]][current_position[1]] == completed:
        movement = input("Which direction do you want to move?\n>>> ")
        current_position = move(movement, initial_position)

    ghost1 = checkGhost(createBoard[1], createBoard[2])
    ghost2 = checkGhost(createBoard[1], createBoard[2])
    while ghost1 == ghost2 and ghost1 != None and ghost2 != None:
        ghost2 = checkGhost(createBoard[1], createBoard[2])

    current_position = [board[0][current_position[0]][current_position[0]], board[0][current_position[0]][current_position[1]]]
    if ghost1 != None or ghost2 != None:
        createBoard[0][current_position[0]][current_position[1]] = ghost
        drawBoard()
        print("You encountered a Ghost! Now you'll have to answer two questions to leave this room.\n")
        for _ in range(2):
            true_or_false = validateRiddle(True, current_position)
            if true_or_false == False:
                break

    elif current_position == createBoard[2]:
        createBoard[0][current_position[0]][current_position[1]] = found_candy
        drawBoard()
        print("You found the candy! Game over.")
        break

    else:
        print("To move to the next room, you'll have to answer the following question:\n")
        true_or_false = validateRiddle(False, current_position)
        if true_or_false == False:
            break

