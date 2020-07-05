'''
Created on Oct 7, 2018

@author: swagatam
'''
count = 0
def tie(state) :
    flag=True
    for i in range(0,3):
        for j in range(0,3):
            if(state[i][j]=="_"):
                return False;
    return flag

def win(state):
    for i in range(0,3):
        if state[i][0] == state[i][1] == state[i][2] and (state[i][0]=="X" or state[i][0]=="O"):
            if state[i][0]=="X":
                return "X";
            else:
                return "O";
    for i in range(0,3):
        if state[0][i] == state[1][i] == state[2][i] and (state[0][i]=="X" or state[0][i]=="0"):
            if state[0][i]=="X":
                return "X"
            else:
                return "O"
    
    if state[0][0]==state[1][1] and state[1][1]==state[2][2] and (state[0][0]=="X" or state[0][0]=="O"):
            if state[0][0]=="X":
                return "X"
            else:
                return "O"
    if state[0][2] == state[1][1] == state[2][0] and (state[0][2]=="X" or state[0][2]=="O"):
        if state[0][2]=="X":
            return "X"
        else:
            return "O"
    
def eval(state):
    if win(state)=="X":
            return 1
    elif win(state)=="O":
            return -1;
    #return 0
    
    
def minmax(state,player,alpha,beta):
    if eval(state)==1:
        return 1
    elif eval(state)==-1:
        return -1
    elif tie(state):
        return 0;
    
    if player=="max":
        val=alpha
        for i in range(0,3):
            for j in range(0,3):
                if state[i][j]=="_":
                    state[i][j]="X"
                    global count
                    count = count +1
                    value = minmax(state,"min",alpha,beta)
                    val = max(val,value)
                    alpha = max(alpha,val)
                    state[i][j]="_"
                    if beta <= alpha :
                        break
                    #print(val)
        return val
    
    if player=="min":
        val=9999
        for i in range(0,3):
            for j in range(0,3):
                if state[i][j]=="_":
                    state[i][j]="O"
                    count = count +1
                    value = minmax(state,"max",-9999,9999)
                    val = min(val,value)
                    beta = min(beta,val)
                    state[i][j]="_"
                    if beta <= alpha :
                        break
        return val
    
def nextmove(state):
    bestval=9999
    nextX = -1
    nextY = -1
    for i in range(0,3):
        for j in range(0,3):
            if state[i][j]=="_":
                state[i][j]="O"
                global count
                count = count+1
                val=minmax(state,"max",-9999,9999)
                #print(val)
                #print(state)
                if bestval>val:
                    bestval=val
                    nextX=i 
                    nextY=j
                state[i][j]="_"
    state[nextX][nextY]="O"
    return state

#state=[[] for i in range(0,3)]
state = [["_","_","_"],["_","_","_"],["_","_","_"]]
#for i in range(0,3):
#    for j in range(0,3):
#        state[i][j]=" "
        
def printstate(state):
    for i in range(0,3):
        for j in range(0,3):
            #print("| ")
            print(state[i][j]," ")
        print("\n")
        
i=0
while(True):
    print("Enter the pos of X:")
    v =input().split(" ")
    state[int(v[0])][int(v[1])]="X"
    #printstate(state)
    #state=[["X","O","X"],["X","X","O"],["O","_","_"]]
    #for i in range(0,3):
    #   for j in range(0,3):
    #        if state[i][j]=="X":
    #            print(i,j)
    
    print("current state is: ")
    print(state)
    
    if win(state):
        print("X wins")
        break
    elif tie(state):
        print("Tie")
        break
    else:
        state=nextmove(state)
        if i ==0:
            print("Number of nodes created: ",count)
            i = i+1
        #printstate(state)
        print("next move")
        print(state)
        if win(state):
            print("B wins")
            break
        if tie(state):
            print("Tie")
            break