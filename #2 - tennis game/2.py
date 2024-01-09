"""
Write a program that shows how a tennis game progresses and who has won. The program will receive a sequence formed by "P1" (Player 1) or "P2" (Player 2), indicating who wins each point of the game.

- The scores in a game are "Love" (zero), 15, 30, 40, "Deuce" (tie), advantage.
- Given the sequence [P1, P1, P2, P2, P1, P2, P1, P1], the program would display the following:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Advantage P1
  Player 1 has won

- If you wish, you can handle errors in the input data.
- Refer to the rules of the game if you have doubts about the scoring system.
"""

player1 = "P1"
player1_points = 0

player2 = "P2"
player2_points = 0

secuence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]


def puntuation(player, player_points):

    player_game_points = []

    for i in secuence:

        if i == player:

            if player_points < 30:
                player_points += 15
            else:
                player_points += 10

        else:
            pass

        player_game_points.append(player_points)

    return player_game_points


def compare_game_points(game_points_1, game_points_2):

    index = 0
    for i in game_points_1:

        if i > 30 and i == game_points_2[index]:
            print("Deuce")
        elif i > 50 and i > game_points_2[index]:
            print("Ha Ganado P1")
        elif i > 40 and i > game_points_2[index]:
            print("Ventaja P1")
        elif game_points_2[index] > 50 and i < game_points_2[index]:
            print("Ha Ganado P2")
        elif game_points_2[index] > 40 and i < game_points_2[index]:
            print("Ventaja P2")

        else:
            if i == 0:
                i = "Love"
            elif game_points_2[index] == 0:
                game_points_2[index] = "Love"

            print(f"{i} | {[i for i in game_points_2][index]}")

        index += 1


compare_game_points(puntuation(player1, player1_points),
                    puntuation(player2, player2_points))
