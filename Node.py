class Node:

    def __init__(self,listOfTokens):
        self.listOfTokens = listOfTokens

    #TODO add heuristic for return of eval of the node
    def getEvalNumber(self, player):
        if player is "maxPlayer":
            print("do max Player eval")
        else:
            print("do min Player eval")
        #use number, as number of token
        return 0