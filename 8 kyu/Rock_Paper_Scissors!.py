'''
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
'''

def rps(p1, p2):
    lista=["rock","paper","scissors"]

    if (lista.index(p1)-lista.index(p2))==1:
        return "Player 1 won!"
    if (lista.index(p1)-lista.index(p2))==-2:
        return "Player 1 won!"
    if (lista.index(p1)-lista.index(p2))==0:
        return "Draw!"
    else:
        return "Player 2 won!"