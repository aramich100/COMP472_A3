import playTheGame
import alphaBeta
from Node import Node

if __name__ == "__main__":

    gameOrAlgo = input("Would you like to play the game or run the algo?")

    if "game" in gameOrAlgo.lower():
        l = [2,3,4,5,6,7]
        N = Node(l, 4)
        print(N.getEvalNumber("maxplayer"))