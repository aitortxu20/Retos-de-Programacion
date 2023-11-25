"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

list = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]

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