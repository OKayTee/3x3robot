from Scramble import scramble
from solgen import getsolution
import sys, getopt

algorithm=""

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"brs:")
    except getopt.GetoptError:
            print("command argument error")

            sys.exit(2)
    for opt, arg in opts:
        if opt == "-r":
            algorithm = getsolution()
            #print(algorithm)
            solve(algorithm)
            sys.exit(0)
        elif opt == "-s":
            algorithm = scramble()
            print(algorithm)
            sys.exit(0)
        elif opt == "-b":
            algorithm = scramble()
            print(algorithm)
            algorithm = getsolution()
            print(algorithm)
            sys.exit(0)
def solve(algo):
    for move in algo:
        stepper

if __name__ == "__main__":
    main(sys.argv[1:])
