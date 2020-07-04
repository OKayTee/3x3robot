from Scramble import scramble
from solgen import getsolution
import sys, getopt
from Camctrl import calibrate
from stepperctrl import move




def main(argv):
    try:
        opts, args = getopt.getopt(argv,"rscmhu:")
    except getopt.GetoptError:
            print("Command Argument Error")
            print("Run with -h for help")

            sys.exit(2)
    for opt, arg in opts:
        if opt == "-r":  #launch in solve mode
            algorithm = getsolution()
            print(algorithm)
            solve(algorithm)
            sys.exit(0)
        elif opt == "-s":   #launch in scramble mode
            algorithm = scramble()
            print(algorithm)
            solve(algorithm)
            sys.exit(0)
        elif opt == "-c":   #launch in calibrate mode
            calibrate()
        elif opt == "-m":
            while(True):
                turn = input()
                solve(turn)
                if turn == "Q":
                    sys.exit(0)
                    
        elif opt == "-h":
            print("-s   -   scramble mode")
            print("-r   -   resolve mode")
            print("-m   -   manual mode")
            print("-c   -   calibrate mode")
            print("-h   -   display help")
def solve(algorithm):
    for moves in algorithm:
        move(moves)

if __name__ == "__main__":
    main(sys.argv[1:])
