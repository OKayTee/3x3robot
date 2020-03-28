import time
#from adafruit_motorkit import MotorKit

#kit1 = MotorKit() #U,D
#kit2 = MotorKit(address = 0x61) #F,B
#kit3 = MotorKit(address = 0x62) #L,R


def move(moves):
   dictionary[moves]
    
    

def up(ang):
    if ang == 0:
        print("U NORMAL")
    elif ang == 1:
        print("U PRIME")
        
dictionary = {
        "U": up(0),
        "u": up(1)

    }

if __name__ == "__main__":
    inp = "U"
    move(inp)
    inp = "u"
    move(inp)