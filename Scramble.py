from random import randint

moves = ['U','u','V','R','r','X','F','f','W','B','b','Y','L','l','Z','D','d','[']

def rule2(current,previous):
    if current//3 == previous//3:
        return False
    else: return True

def rule3(current, previous1, previous2):
    if ((5-(current//3))==previous1//3) and (current//3 == previous2//3):
        return False
    else: return True

def scramble():
    output = []
    scramblealg=""
    for i in range(30):
        goodmove = False

        while not goodmove: 
            move = randint(0,17)
            if i==0:    #first move is always valid
                goodmove = True
            elif i==1:
                goodmove = rule2(move,output[i-1])
            else:
                goodmove = rule2(move,output[i-1]) and rule3(move,output[i-1],output[i-2])
                
        output.append(move)
    for move in output:
        scramblealg += moves[move]    
    return scramblealg

if __name__ == "__main__":
   test = scramble()
   print(test)