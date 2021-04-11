import playTheGame
import alphaBeta
import Node
import copy

if __name__ == "__main__":

    gameOrAlgo = input("Would you like to play the game or run the algo?")

    if "game" in gameOrAlgo.lower():
        l = [2,3,4,5,6,7]
        N = Node(l, 4)
        print(N.getEvalNumber("maxplayer"))
    elif "algo" in gameOrAlgo.lower():
        print("andre is a bitch")

        # TODO get user inputs.
        #  PNT Player <#tokens> <#taken_tokens> <list_of_taken_tokens> <depth>
        #  this can be done either by asking the user or by taking in a file.
        #  can also just be hard coded... in format like [7,2,3,6,0]

        # TODO run the alphabeta algo
        #  in the alphabeta algo, the prints for the outputs will be done
        fullList = [1,2,3,4,5]
        cutList = [1,2]
        nodes = []
        for num in cutList:
            tempList = copy.deepcopy(fullList)
            tempList.remove(num)
            alpha = Double.NEGATIVE_INFINITY
            beta = Double.Positive_Infinity
            alphaBeta.miniMax(Node(num, tempList), "depth", alpha, beta, "maxPlayer")

    else:
        exit()
