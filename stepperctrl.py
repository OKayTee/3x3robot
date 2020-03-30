import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit1 = MotorKit() #U,D
kit2 = MotorKit(address = 0x61) #F,B
kit3 = MotorKit(address = 0x62) #L,R


def move(moves):
   dictionary[moves]
    
    

def up(ang):
    if ang == 0:
        for i in range(50):
            kit1.stepper1.onestep()
            time.sleep(0.01)
    elif ang == 1:
        for i in range(50):
            kit1.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
    elif ang == 2:
        for i in range(100):
            kit1.stepper1.onestep()
            time.sleep(0.01)

def down(ang):
    if ang == 0:
        for i in range(50):
            kit1.stepper2.onestep()
            time.sleep(0.01)
    elif ang == 1:
        for i in range(50):
            kit1.stepper2.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
    elif ang == 2:
        for i in range(100):
            kit1.stepper2.onestep()
            time.sleep(0.01)
          
def front(ang):
    if ang == 0:
        for i in range(50):
            kit2.stepper1.onestep()
            time.sleep(0.01)
    elif ang == 1:
        for i in range(50):
            kit2.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
    elif ang == 2:
        for i in range(100):
            kit2.stepper1.onestep()
            time.sleep(0.01)
def behind(ang):
    if ang == 0:
        for i in range(50):
            kit2.stepper2.onestep()
            time.sleep(0.01)
    elif ang == 1:
        for i in range(50):
            kit2.stepper2.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
    elif ang == 2:
        for i in range(100):
            kit2.stepper2.onestep()
            time.sleep(0.01)

def left(ang):
    if ang == 0:
        for i in range(50):
            kit3.stepper1.onestep()
            time.sleep(0.01)
    elif ang == 1:
        for i in range(50):
            kit3.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
    elif ang == 2:
        for i in range(100):
            kit3.stepper1.onestep()
            time.sleep(0.01)

def right(ang):
    if ang == 0:
        for i in range(50):
            kit3.stepper2.onestep()
            time.sleep(0.01)
    elif ang == 1:
        for i in range(50):
            kit3.stepper2.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
    elif ang == 2:
        for i in range(100):
            kit3.stepper2.onestep()
            time.sleep(0.01)

dictionary = {
        "U": up(0),
        "u": up(1)
        "F": front(0)
        "f": front(1)
        "R": right(0)
        "r": right(1)
        "B": behind(0)
        "b": behind(1)
        "L": left(0)
        "l": left(1)
        "D": down(0)
        "d": down(1)
        "V": up(2)
        "W": front(2)
        "X": right(2)
        "Y": behind(2)
        "Z": left(2)
        "[": down(2)
        
    }