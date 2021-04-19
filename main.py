import math
from tokenize import Double

import playTheGame
import alphaBeta
from node import *
import copy

class Statistic:

    def __init__(self):
        self.nodesVisited = 0
        self.nodesEvaluated = 0
        self.deepest = math.inf

if __name__ == "__main__":
    gameOrAlgo = input("Would you like to play the game or run the algo?")
    if "game" in gameOrAlgo.lower():
        l = [2,3,4,5,6,7]
        N = node(l, 4, -1)
        print(N.getEvalNumber("maxplayer"))
    elif "algo" in gameOrAlgo.lower():
        # TODO get user inputs.
        #  PNT Player <#tokens> <#taken_tokens> <list_of_taken_tokens> <depth>
        #  this can be done either by asking the user or by taking in a file.
        #  can also just be hard coded... in format like [7,2,3,6,0]

        # TODO run the alphabeta algo
        #  in the alphabeta algo, the prints for the outputs will be done
        fullList = [1,2,3,4,5]
        cutList = [1,2]
        values = []
        stats = Statistic()
        for num in cutList:
            tempList = copy.deepcopy(fullList)
            tempList.remove(num)
            alpha = -math.inf
            beta = math.inf
            values.append(alphaBeta.miniMax(Node(tempList, num,""), 10, alpha, beta, "maxplayer",stats))
        
        for value in values:
            print(value)

    else:
        exit()
