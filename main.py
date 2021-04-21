import math
from tokenize import Double

import playTheGame
import alphaBeta
from node import *
import copy
import re


class Statistic:

    def __init__(self):
        self.nodesVisited = 0
        self.nodesEvaluated = 0
        self.deepest = math.inf

def printOutput(node,stats,value):
    print("Move: ", node.move)
    print("Value: ", value)
    print("Number of Nodes Visited: ", stats.nodesVisited)
    print("Number of Nodes Evaluated: ", stats.nodesEvaluated)
    print("Max Depth Reached: ", stats.deepest)
    print("Avg Effective Branching Factor: ", "andre?")

if __name__ == "__main__":
    gameInput = input("Would you like to play the game or run the algo?")
    gameInput = [int(i) for i in gameInput.split() if i.isdigit()]
    tokens = int(gameInput[0])
    taken_tokens = int(gameInput[1])
    list_of_taken_tokens = []
    if taken_tokens > 0:
        list_of_taken_tokens = [int(i) for i in gameInput[2:taken_tokens+2]]
    depth = gameInput[len(gameInput) - 1]

    if depth == 0:
        depth = math.inf

    fullList = list(range(1, tokens+1))

    cutList = None
    if taken_tokens == 0:
        initalNode = Node(fullList,0,"")
        cutList = alphaBeta.possibleMoves(initalNode)
    else:
        for num in list_of_taken_tokens:
            fullList.remove(num)
        initalNode = Node(fullList, list_of_taken_tokens[len(list_of_taken_tokens)-1], "")
        cutList = alphaBeta.possibleMoves(initalNode)

    player = "maxplayer"
    if taken_tokens % 2 == 1:
        player = "minplayer"

    values = []
    stats = Statistic()
    for num in cutList:
        tempList = copy.deepcopy(fullList)
        tempList.remove(num)
        alpha = -math.inf
        beta = math.inf
        values.append(alphaBeta.miniMax(Node(tempList, num, ""), depth, alpha, beta, player, stats))
    for i in values:
        print(i)