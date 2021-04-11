class Node:

    def __init__(self,listOfTokens,move):
        self.listOfTokens = listOfTokens
        self.move = move

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
    def getSuccesorCount(self, move):
        count = 0
        for i in range(len(self.listOfTokens)):
            if move > self.listOfTokens[i]:
                if (move % self.listOfTokens[i] == 0):
                    count += 1

            if move < self.listOfTokens[i]:
                if (self.listOfTokens[i] % move == 0):
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

    #TODO add heuristic for return of eval of the node
    def getEvalNumber(self, player):
        if player is "maxPlayer":
            print("do max Player eval")
        else:
            print("do min Player eval")
        #use number, as number of token
        return 0