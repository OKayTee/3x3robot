from random import randint

moves = ['U','u','F','f','R','r','B','b','L','l','D','d','V','W','X','Y','Z','[']
opposites = ['D','d','B','b','L','l','F','f','R','r','U','u','[','Y','Z','W','X','V']
doubles = ['V','W','X','Y','Z','[']
def scramble():
    output = ""
    for i in range(30):
        good = 0
        while good == 0: 
            move = randint(0,17)
            if i>0:
                if move<12:
                    if (move % 2)==0:
                        if (output[i-1] != moves[move]) and (output[i-1] != moves[move+1] and output[i-1] != doubles[move//2]): #implementing rule 2
                            if (output[i-1] == opposites[move]) or (output[i-1] == opposites[move+1]):
                                if output[i-2] != moves[move] and output[i-2] != moves[move+1]:
                                    output+=moves[move]
                                    good = 1
                            else:
                                output+=moves[move]
                                good = 1
                    else:
                        if (output[i-1] != moves[move]) and (output[i-1] != moves[move-1] and output[i-1] != doubles[move//2]):
                            if (output[i-1] == opposites[move]) or (output[i-1] == opposites[move-1]):
                                if output[i-2] != moves[move] and output[i-2] != moves[move-1]:
                                    output+=moves[move]
                                    good = 1
                            else:
                                output+=moves[move]
                                good = 1
                else:
                    if (output[i-1] != moves[move]) and (output[i-1] != moves[(move-12)//2]) and (output[i-1] != moves[((move-12)//2)+1]) :
                        output+=moves[move]
                        good = 1
            else:
                    output+=moves[move]  #first move is always valid
                    good = 1
    return output

if __name__ == "__main__":
    lol = scramble()
    print(lol)