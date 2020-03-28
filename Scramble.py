from random import randint

moves = ['U','u','F','f','L','l','R','r','B','b','D','d','1','2','3','4','5','6']

def scramble():
    output = ""
    for i in range(30):
        good = 0
        while good == 0: 
            move = randint(0,17)
            if i>0:
                if move<12:
                    if (move % 2)==0:
                        if (output[i-1] != moves[move]) and (output[i-1] != moves[move+1]): 
                            output+=moves[move]
                            good = 1
                    else:
                        if (output[i-1] != moves[move]) and (output[i-1] != moves[move-1]):
                            output+=moves[move]
                            good = 1
                else:
                    if output[i-1] != moves[move]:
                        output+=moves[move]
                        good = 1
            else:
                    output+=moves[move]
                    good = 1
    return output