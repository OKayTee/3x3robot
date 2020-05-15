import cv2
from PIL import Image
import numpy as np
import colorsys
import json

coords = json.loads(open("training_coords.json").read())
cameras = [0,2,4,6]
def capture():  #open specific webcam and capture an image
    for i in cameras:   
        video_capture = cv2.VideoCapture(i)
        if not video_capture.isOpened():
            raise Exception("Could not open video device")
        ret, frame = video_capture.read()
        cv2.imwrite("test"+i+".png",frame)
        video_capture.release()

def getvalues():
    im = Image.open("training.jpg")
    results = []
    pix = im.load()
    output = []
    for a,b,c in coords:
        z=0
        values = [[0 for cols in range(3)] for rows in range (100)]
        
        for x in range (10):        #collect data from a 10x10 grid
            for y in  range(10):
                values[z][0], values[z][1], values[z][2] = pix[(x+a), (y+b)]
              
                z=z+1
        r,g,b = geomean(values)
        h,s,v = colorsys.rgb_to_hsv(r/255,g/255,b/255)
        h = round(h*360)
        s = round(s*100)
        v = round(v*100)
        results.append([h,s,v,c])   #calculate the geometrical mean of the 100 values and add the result to the output array
    
    results = arrsort(results)
    output = [recognise([h,s,v]) for h,s,v,c in results] #send each element through color recognition
    return output

def getState():
    state = getvalues()
    #insert the colors of the centers into the output
    state.insert(4, 'U')
    state.insert(13, 'R')
    state.insert(22, 'F')
    state.insert(31, 'D')
    state.insert(40, 'L')
    state.insert(49, 'B')
    output = ""
    for move in state:
        output+=move
    return output

def geomean(values):
    r=1
    g=1
    b=1
    for i in range(100):
        r = r*(values[i][0])
        g = g*(values[i][1]) 
        b = b*(values[i][2])
    r= round(np.power(r,(1/100)))
    g= round(np.power(g,(1/100)))
    b= round(np.power(b,(1/100)))
    return r,g,b

def recognise(color):
    red_low = [330,20,30]
    red_low2 = [0,20,30]
    red_high = [360,100,100]
    red_high2 = [20, 100, 100]
    orange_low = [21,20, 30]
    orange_high = [52, 100, 100]
    yellow_low = [53,20,30]
    yellow_high  =[80,100,100]
    green_low = [81,20,30]
    green_high = [145,100,100]
    blue_low = [200,20,30]
    blue_high = [260,100,100]

    
    if between(color,red_low,red_high) or between(color,red_low2,red_high2):
        return "R"
    elif between(color,orange_low,orange_high):
        return "L"
    elif between(color,yellow_low,yellow_high):
        return "D" 
    elif between(color,green_low,green_high):
        return "F"    
    elif between(color, blue_low, blue_high):
        return "B"
    else:
        return "U"

def between(src,lower,upper): #check if input value is between other two values 
    if src[0]>=lower[0] and src[0]<=upper[0] and src[1]>=lower[1] and src[1]<=upper[1] and src[2]>=lower[2] and src[2]<=upper[2]:
        return True
    else:
        return False

def arrsort(arr):       #sort the array of coordinates to correspond with the tile order the solving algorithm requires
    isSorted = False
    while  not isSorted:
        isSorted= True
        for i in range(len(arr)):
            if i>0:
                if arr[i][3]<arr[i-1][3]:
                    buffer = arr[i]
                    arr[i] = arr[i-1]
                    arr[i-1] = buffer
                    isSorted = False
    return arr

def calibrate():
    i=0
    coordpos = 0
    for camera in cameras:
        video = cv2.VideoCapture(camera)
        while(True):
            ret, frame = video.read()
            i=coordpos
            while(coords[i][3]==camera):
                cv2.rectangle(frame,(coords[i][0],coords[i][1]),(coords[i][0]+10,coords[i][1]+10),(0,0,0),-1) 
                #for each coordinate to be observed place a rectangle on the window
                i+=1
            cv2.imshow("Calibrate",frame)
            key=cv2.waitKey(1)
            coordpos =  i
            if key == ord('q'):
                break

if __name__ =="__main__":
        calibrate()