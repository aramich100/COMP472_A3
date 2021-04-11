class Node:

    def __init__(self,listOfTokens,move):
        self.listOfTokens = listOfTokens
        self.move = move

    #TODO add heuristic for return of eval of the node
    def getEvalNumber(self, player):
        if player.lowercase() == "maxplayer":
            print("do max Player eval")
        elif player.lowercase() == "minplayer":
            print("do min Player eval")
        #use number, as number of token
        return 0