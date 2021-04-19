import copy
import math
from node import *

# class Statistic:
#     def __init__(self):


# TODO implement function for possible moves
def possibleMoves(node):
    length = len(node.listOfTokens)
    maxNum = max(node.listOfTokens)

    moves = []
    # Not the first move
    if maxNum > length:
        for num in node.listOfTokens:
            if num % node.move == 0 or node.move % num == 0:
                if num != node.move:
                    moves.append(num)
    return moves


# TODO implement minimax, alpha-beta pruning algorithm
# record values for the print out
def miniMax(node, depth, alpha, beta, player,stats):

    if depth == 0 or len(node.listOfTokens) == 1:
        return node.getEvalNumber(player)

    stats.nodesVisited = stats.nodesVisited + 1
    if player == "maxplayer":
        maxEval = -math.inf
        for childNum in possibleMoves(node):
            node1 = createNode(node, childNum)
            eva = miniMax(node1, depth - 1, alpha, beta, "minplayer",stats)
            maxEval = max(maxEval, eva)
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for childNum in possibleMoves(node):
            node1 = createNode(node, childNum)
            eva = miniMax(node1, depth - 1, alpha, beta, "maxplayer",stats)
            minEval = min(minEval, eva)
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval


def createNode(node, childNum):
    tempList = copy.deepcopy(node.listOfTokens)
    tempList.remove(childNum)
    return Node(tempList, childNum, node.lastMoves + str(node.move))


# TODO print out the result of the alphabeta algo
# The best move (i.e., the tokens number that is to be taken) for the current player (as computed by your
# alpha-beta algorithm)
# The value associated with the move (as computed by your alpha-beta algorithm)
# The total number of nodes visited
# The number of nodes evaluated (either an end game state or the specified depth is reached)
# The maximum depth reached (the root is at depth 0)
# The average effective branching factor (i.e., the average number of successors that are not pruned)

def printOutput():
    print("Move: ", "andre?")
    print("Value: ", "andre?")
    print("Number of Nodes Visited: ", "andre?")
    print("Number of Nodes Evaluated: ", "andre?")
    print("Max Depth Reached: ", "andre?")
    print("Avg Effective Branching Factor: ", "andre?")
