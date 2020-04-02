import cv2
from PIL import Image
import numpy as np
import colorsys

def capture():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    ret, frame = video_capture.read()
    cv2.imwrite("test.png",frame)
    video_capture.release()

def recog():
    im = Image.open("test.png")
    
    pix = im.load()
    values = [[0 for a in range(3)] for b in range (100)]
    valueshsv = [[0.0 for a in range(3)] for b in range(100)]
    z=0
    for x in range (10):
        for y in  range(10):
            
            values[z][0], values[z][1], values[z][2] = pix[(x+236), (y+330)]
            valueshsv[z][0], valueshsv[z][1], valueshsv[z][2] = colorsys.rgb_to_hsv((values[z][0]/255),(values[z][1]/255),(values[z][2]/255))
            valueshsv[z][0] = valueshsv[z][0]*360
            valueshsv[z][1] = valueshsv[z][1]*100
            valueshsv[z][2] = valueshsv[z][2]*100
            z=z+1
    r,g,b = geomean(values)
    h,s,v = geomean(valueshsv)
    print(r," ", g, " ", b)
    print(h," ",s," ", v)

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


if __name__ =="__main__":
        recog()