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
        self.deepest = 0


def printOutput(move, value, stats, depth):
    print("Move: ", move)
    print("Value: ", value)
    print("Number of Nodes Visited: ", stats.nodesVisited)
    print("Number of Nodes Evaluated: ", stats.nodesEvaluated)
    print("Max Depth Reached: ", str(depth - stats.deepest))
    print("Avg Effective Branching Factor: ", "?")


if __name__ == "__main__":
    gameInput = input("Would you like to play the game or run the algo?")
    gameInput = [int(i) for i in gameInput.split() if i.isdigit()]
    tokens = int(gameInput[0])
    taken_tokens = int(gameInput[1])
    list_of_taken_tokens = []
    if taken_tokens > 0:
        list_of_taken_tokens = [int(i) for i in gameInput[2:taken_tokens + 2]]
    depth = gameInput[len(gameInput) - 1]

    if depth == 0:
        depth = math.inf

    fullList = list(range(1, tokens + 1))

    cutList = []
    if taken_tokens == 0:
        initalNode = Node(fullList, 0, "")
        cutList = alphaBeta.possibleMoves(initalNode)
    else:
        for num in list_of_taken_tokens:
            fullList.remove(num)
        initalNode = Node(fullList, list_of_taken_tokens[len(list_of_taken_tokens) - 1], "")
        cutList = alphaBeta.possibleMoves(initalNode)

    player = "minplayer"
    if taken_tokens % 2 == 1:
        player = "maxplayer"

    values = []
    stats = Statistic()
    stats.deepest = depth

    alpha = -math.inf
    beta = math.inf
    for num in cutList:
        tempList = copy.deepcopy(fullList)
        tempList.remove(num)
        stats.nodesVisited += 1
        values.append(alphaBeta.miniMax(Node(tempList, num, ""), depth, alpha, beta, player, stats))

    if player == "maxplayer":
        index = values.index(min(values))
        printOutput(cutList[index], values[index], stats, depth)
    else:
        index = values.index(max(values))
        printOutput(cutList[index], values[index], stats, depth)
