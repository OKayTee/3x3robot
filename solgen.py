import kociemba
from Camctrl import getState
doubles = "UFRBLD"
def getsolution():
    try:
        state = getState()
        output = kociemba.solve(state)
    except ValueError:
        print("Invalid cubestring, invalid info from color recognition.")
        print(state)
        sys.exit(0)

    print("########################################################\nGenerated solution:\n")
    print(output+"\n")
    print("########################################################\n")

    
    
    while output.find("'") != -1:
        pos = output.find("'")
        output = output[:pos-1] + output[pos-1].lower() + output[pos:]
        output = output.replace("'","",1)
    
    
    while output.find("2") != -1:
        pos = output.find("2")-1
        
        output = output[:pos]+chr(doubles.find(output[pos])+86) + output[pos+1:]
        
        output = output.replace("2","",1)
    #print(output)
    output = output.replace(" ","") #remove spaces
    return output
#if __name__ == "__main__":
    #getsolution()