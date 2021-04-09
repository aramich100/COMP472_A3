


def createList(r1, r2):
  
    # Testing if range r1 and r2 
    # are equal
    if (r1 == r2):
        return r1
  
    else:
  
        # Create empty list
        res = []
  
        # loop to append successors to 
        # list until r2 is reached.
        while(r1 < r2+1 ):
              
            res.append(r1)
            r1 += 1
        return res


n = 7
list1 = createList(1,7)
moveCount = 0

# Checks if it is the first move
def checkIf_firstMove():
    if(moveCount > 0):
        return False
    
    return True

# Checks if the first move is valid
def isValid_firstMove(m):
    if(m > (n/2)):
        return False
    
    return True


def firstMove(moveCount):
    while checkIf_firstMove:
        firstMove = int(input("Player 1, enter your first move! \n"))

        if(isValid_firstMove(firstMove)):
            moveCount = moveCount + 1
            list1.remove(firstMove)
            break


def game():
    print("\n Available tokens : ")
    print(*list1)
    print()
    while True:
        player2 = int(input("Player 2, enter your move\n"))


print("\n --- GAME HAS STARTED ---")
print("\n Available tokens : ")
print(*list1)
print()
firstMove(moveCount)
print(*list1)

