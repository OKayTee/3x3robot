import cv2
from PIL import Image
import numpy as np
import colorsys
import json

coords = json.loads(open("training_coords.json").read())

def capture():  #open specific webcam and capture an image
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    ret, frame = video_capture.read()
    cv2.imwrite("test.png",frame)
    video_capture.release()

def getvalues():
    im = Image.open("training.jpg")
    results = []
    pix = im.load()
    output = []
    for a,b,c in coords:
        z=0
        values = [[0 for cols in range(3)] for rows in range (100)]
        #valueshsv = [[0.0 for cols in range(3)] for rows in range(100)]
        for x in range (10):        #collect data from a 10x10 grid for accuracy
            for y in  range(10):
                
                values[z][0], values[z][1], values[z][2] = pix[(x+a), (y+b)]
               # valueshsv[z][0], valueshsv[z][1], valueshsv[z][2] = colorsys.rgb_to_hsv((values[z][0]/255),(values[z][1]/255),(values[z][2]/255)) #convert all values to hsv
               # valueshsv[z][0] = valueshsv[z][0]*360
                #valueshsv[z][1] = valueshsv[z][1]*100
                #valueshsv[z][2] = valueshsv[z][2]*100
                z=z+1
        r,g,b = geomean(values)
        h,s,v = colorsys.rgb_to_hsv(r/255,g/255,b/255)
        h = round(h*360)
        s = round(s*100)
        v = round(v*100)
        results.append([h,s,v])   #calculate the geometrical mean of the 100 values and add the result to the output array
    print(results)
    output = [recognise(result) for result in results]
    print(output)

def getState():
    output = 'FULDUDRDRUFBFRLURDFLBUFRRBBBDLLDULLRLRUBLBDBDDFUFBRFUF'
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
        return "red"
    elif between(color,orange_low,orange_high):
        return "orange"
    elif between(color,yellow_low,yellow_high):
        return "yellow" 
    elif between(color,green_low,green_high):
        return "green"    
    elif between(color, blue_low, blue_high):
        return "blue"
    else:
        return "white"

def between(src,lower,upper):
    if src[0]>=lower[0] and src[0]<=upper[0] and src[1]>=lower[1] and src[1]<=upper[1] and src[2]>=lower[2] and src[2]<=upper[2]:
        return True
    else:
        return False

if __name__ =="__main__":
        getvalues()