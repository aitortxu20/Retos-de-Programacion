# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

match = True
score = ["Love", "15", "30", "40", "Deuce", "ventaja"]
P1_score = []
P2_score = []
score_text = ["Love", "Love"]
var = 0

def check_match(var, player, var2, opponent):
    global match, score_text

    if len(var) == 1:
        score_text[player] = "15"
    elif len(var) == 2:
        score_text[player] = "30"
    elif len(var) == 3:
        if len(var) == len(var2):
            score_text = ["Deuce", "Deuce"]
        else:
            score_text[player] = "40"
    else:
        if len(var) == len(var2):
            score_text = ["Deuce", "Deuce"]
        elif (len(var) - len(var2)) < 2:
            score_text[player] = "Ventaja"
            score_text[opponent] = "40"
        else:
            if len(P1_score) > len(P2_score):
                print("Player 1 won!")
            else:
                print("Player 2 won!")
            match = False

def score_input():
    global match, P1_score, P2_score, var

    print(f"Score is: P1   {score_text[0]} - {score_text[1]}   P2")

    var = input("Who scored? (1/2)\n>>> ")
    if var == "1":
        P1_score.append(var)
        var = P1_score
        var2 = P2_score
        check_match(var, 0, var2, 1)
    elif var == "2":
        P2_score.append(var)
        var = P2_score
        var2 = P1_score
        check_match(var, 1, var2, 0)
    else:
        print("This is not a valid player")

while match:
    
    score_input()

