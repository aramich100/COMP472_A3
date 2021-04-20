import copy

class Node:

    def __init__(self,listOfTokens, move, lastMoves):
        self.listOfTokens = listOfTokens
        self.move = move
        self.lastMoves = lastMoves # array of last Moves

    # Returns if move is a prime or not
    def isPrime(self,num):
        flag = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
        if flag:
            return False
        else:
            return True


    # Returns number of succesors
    def getSuccesorCount(self, move, listok):
        count = 0
        for i in range(len(listok)):
            if move > listok[i]:
                if (move % listok[i] == 0):
                    count += 1

            if move < listok[i]:
                if (listok[i] % move == 0):
                    count += 1

        return count+1

    # Returns largest prime that is a succesor
    def getLargestPrime(self, move):
        largestPrime = 1

        for i in range(len(self.listOfTokens)):
            if self.isPrime(i):
                if i>largestPrime:
                    if self.getSuccesorCount(i)>0:
                        largestPrime = i

        return largestPrime

    def isGameOver(self, move):
        tempList = copy.deepcopy(self.listOfTokens)
        tempList.remove(move)
        # If count is 1, game is over
        if(getSuccesorCount(move, tempList) == 1):
            return True
        
        return False




    #TODO add heuristic for return of eval of the node
    def getEvalNumber(self, player):
        if player == "maxPlayer":

            if isGameOver(self.move, self.listOfTokens):
                return -1

            # TOKEN 1 NOT TAKEN
            if 1 in self.listOfTokens:
                return 0

            # LAST MOVE WAS 1
            if (self.move == 1):
                possibleSuccesorsCount = len(self.listOfTokens) - 1
                if (possibleSuccesorsCount % 2 == 0):
                    return -0.5
                else:
                    return 0.5

            # LAST MOVE WAS PRIME
            if (self.isPrime(self.move)):
                count = self.getSuccesorCount(self.move,self.listOfTokens)
                if (count % 2 == 0):
                    return -0.7
                else:
                    return -0.7

            # LAST MOVE WAS COMPOSITE
            if (not (self.isPrime(self.move))):
                largestPrime = self.getLargestPrime(self.move)
                count = self.getSuccesorCount(largestPrime,self.listOfTokens)
                if (count % 2 == 0):
                    return -0.6
                else:
                    return 0.6

        else:
            # TOKEN 1 NOT TAKEN

            if isGameOver(self.move, self.listOfTokens):
                return 1

            if 1 in self.listOfTokens:
                return 0

            # LAST MOVE WAS 1
            if (self.move == 1):
                possibleSuccesorsCount = len(self.listOfTokens) - 1
                if (possibleSuccesorsCount % 2 == 0):
                    return 0.5
                else:
                    return -0.5

            # LAST MOVE WAS PRIME
            if (self.isPrime(self.move)):
                count = self.getSuccesorCount(self.move,self.listOfTokens)
                if (count % 2 == 0):
                    return 0.7
                else:
                    return -0.7

            # LAST MOVE WAS COMPOSITE
            if (not (self.isPrime(self.move))):
                largestPrime = self.getLargestPrime(self.move)
                count = self.getSuccesorCount(largestPrime,self.listOfTokens)
                if (count % 2 == 0):
                    return 0.6
                else:
                    return -0.6
        return 0