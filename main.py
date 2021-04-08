
n = 7
list1 = range(1,n)
moveCount = 0

def checkIf_firstMove():
    if(moveCount > 0):
        return False
    
    return True

def isValid_firstMove(m):
    if(m > (n/2)):
        return False
    
    return True

print(isValid_firstMove(2))