import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit1 = MotorKit() #U,D
kit2 = MotorKit(address = 0x61) #F,B
kit3 = MotorKit(address = 0x62) #L,R

'''
        "U": up(0),
        "u": up(1),
        "F": front(0),
        "f": front(1),
        "R": right(0),
        "r": right(1),
        "B": behind(0),
        "b": behind(1),
        "L": left(0),
        "l": left(1),
        "D": down(0),
        "d": down(1),
        "V": up(2),
        "W": front(2),
        "X": right(2),
        "Y": behind(2),
        "Z": left(2),
        "[": down(2)
'''
def move(moves):
    if moves == "U":
        up(0)
    elif moves == "u":
        up(1)
    elif moves == "V":
        up(2)
    elif moves == "F":
        front(0)
    elif moves == "f":
        front(1)
    elif moves == "W":
        front(2)
    elif moves == "R":
        right(0)
    elif moves == "r":
        right(1)
    elif moves == "X":
        right(2)
    elif moves == "B":
        behind(0)
    elif moves == "b":
        behind(1)
    elif moves == "Y":
        behind(2)
    elif moves == "L":
        left(0)
    elif moves == "l":
        left(1)
    elif moves == "Z":
        left(2)
    elif moves == "D":
        down(0)
    elif moves == "d":
        down(1)
    elif moves == "[":
        down(2)
    time.sleep(0.1)

def up(ang):
    if ang == 0:
        for i in range(100):
            kit1.stepper1.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
        
    elif ang == 1:
        for i in range(100):
            kit1.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
        
    elif ang == 2:
        for i in range(200):
            kit1.stepper1.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    kit1.stepper1.release()

def down(ang):
    if ang == 0:
        for i in range(100):
            kit1.stepper2.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 1:
        for i in range(100):
            kit1.stepper2.onestep(direction=stepper.BACKWARD, style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 2:
        for i in range(200):
            kit1.stepper2.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    kit1.stepper2.release()  

def front(ang):
    if ang == 0:
        for i in range(100):
            kit2.stepper1.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 1:
        for i in range(100):
            kit2.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 2:
        for i in range(200):
            kit2.stepper1.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    kit2.stepper1.release()

def behind(ang):
    if ang == 0:
        for i in range(100):
            kit2.stepper2.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 1:
        for i in range(100):
            kit2.stepper2.onestep(direction=stepper.BACKWARD, style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 2:
        for i in range(200):
            kit2.stepper2.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    kit2.stepper2.release()

def left(ang):
    if ang == 0:
        for i in range(100):
            kit3.stepper1.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 1:
        for i in range(100):
            kit3.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 2:
        for i in range(200):
            kit3.stepper1.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    kit3.stepper1.release()

def right(ang):
    if ang == 0:
        for i in range(100):
            kit3.stepper2.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 1:
        for i in range(100):
            kit3.stepper2.onestep(direction=stepper.BACKWARD, style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    elif ang == 2:
        for i in range(200):
            kit3.stepper2.onestep(style = stepper.INTERLEAVE)
            if i<10:
                time.sleep(0.064-0.005*i)
            else:
                time.sleep(0.01)
    kit3.stepper2.release()
    