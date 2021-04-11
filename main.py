


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

lastMove = 1

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


def firstMove(moveCount, lastMove):
    while checkIf_firstMove:
        firstMove = int(input("Player 1, enter your first move! \n"))

        if(isValid_firstMove(firstMove)):
            moveCount = moveCount + 1
            list1.remove(firstMove)
            lastMove = firstMove
            break


def isMultiple(lastMove, newMove):

    if(newMove > lastMove):
        if(newMove%lastMove == 0):
            return True
    
    elif(lastMove > newMove):
        if(newMove%lastMove == 0):
            return True

    return False

def canWin(lastMove, list1):
    for i in list1:
        print("Last move: ", lastMove)
        print("can win: ", *list1)
        print("i : ",i)
        if(isMultiple(lastMove, int(list1[i]))):
            return True
            break
        
    
    return False



def game(moveCount, lastMove):
    print(" --- First move was made.. Game will now begin --- \n")
    print("\n Available tokens : ")
    print(*list1)
    print()

    while (len(list1) != 0):
        # Player 2
        while canWin(lastMove, list1):
            player2 = int(input("Player 2, enter your move\n"))
            if(isMultiple(lastMove, player2)):
                list1.remove(player2)
                lastMove = player2
                break

        # Player 1
        while canWin(lastMove, list1):
            player1 = int(input("Player 1, enter your move\n"))
            if(isMultiple(lastMove, player1)):
                list1.remove(player1)
                lastMove = player1
                break


print("\n --- GAME HAS STARTED ---")
print("\n Available tokens : ")
print(*list1)
print()
firstMove(moveCount, lastMove)
game(moveCount, lastMove)

