"""
Create a program that calculates who wins more rounds in Rock, Paper, Scissors, Lizard, Spock.

The result can be: "Player 1", "Player 2", "Tie" (draw).
The function receives a list containing pairs, representing each play.
The pair can contain combinations of "🗿" (rock), "📄" (paper), "✂️" (scissors), "🦎" (lizard), or "🖖" (spock).
Example: Input: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Result: "Player 2".
You should look for information on how to play with these 5 possibilities.
"""

list = [("🗿" ,"✂️"), ("✂️" ,"🗿"), (" 📄","✂️")]


def game_winner(list):
    player1 = 0
    player2 = 0

    print(list)

    for play in list:
        if play[0] == "✂️" and play[1] == "📄":
            player1 += 1
        elif play[1] == "✂️" and play[0] == "📄":
            player2 += 1

        elif play[0] == "📄" and play[1] == "🗿":
            player1 += 1
        elif play[1] == "📄" and play[0] == "🗿":
            player2 += 1

        elif play[0] == "🗿" and play[1] == "🦎":
            player1 += 1
        elif play[1] == "🗿" and play[0] == "🦎":
            player2 += 1

        elif play[0] == "🦎" and play[1] == "🖖":
            player1 += 1
        elif play[1] == "🦎" and play[0] == "🖖":
            player2 += 1

        elif play[0] == "🦎" and play[1] == "🖖":
            player1 += 1
        elif play[1] == "🦎" and play[0] == "🖖":
            player2 += 1

        elif play[0] == "🖖" and play[1] == "✂️":
            player1 += 1
        elif play[1] == "🖖" and play[0] == "✂️":
            player2 += 1

        elif play[0] == "🖖" and play[1] == "✂️":
            player1 += 1
        elif play[1] == "🖖" and play[0] == "✂️":
            player2 += 1

        elif play[0] == "✂️" and play[1] == "🦎":
            player1 += 1
        elif play[1] == "✂️" and play[0] == "🦎":
            player2 += 1

        elif play[0] == "🦎" and play[1] == "📄":
            player1 += 1
        elif play[1] == "🦎" and play[0] == "📄":
            player2 += 1

        elif play[0] == "📄" and play[1] == "🖖":
            player1 += 1
        elif play[1] == "📄" and play[0] == "🖖":
            player2 += 1

        elif play[0] == "🖖" and play[1] == "🗿":
            player1 += 1
        elif play[1] == "🖖" and play[0] == "🗿":
            player2 += 1

        elif play[0] == "🗿" and play[1] == "✂️":
            player1 += 1
        elif play[1] == "🗿" and play[0] == "✂️":
            player2 += 1

    if player1 > player2:
        print("Player 1 wins!")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 2 wins!")


game_winner(list)
