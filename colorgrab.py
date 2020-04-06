from PIL import Image
import colorsys

coords = [[1600,900,0],
         [860,1230,0],
         [1538,1720,0],
         [2306,1268,0],
         [1256,1070,1],
         [1300,1500,1],
         [1900,1500,1],
         [1850,1076,1],
         [680,1550,2],
         [1334,2052,2],
         [860,2224,2],
         [1390,2722,2],
         [996,1776,3],
         [768,1900,3],
         [1106,2490,3],
         [1388,2444,3],
         [1768,2158,5],
         [1724,2838,5],
         [2338,2304,5],
         [2526,1600,5],
         [2200, 1868,4],
         [1754,2554,4],
         [2132,2576,4],
         [2428,1986,4]]

def grab():
    im = Image.open("training.jpg")
    
    pix = im.load()
    result=[]
    #values = [[0 for a in range(3)] for b in range (100)]
    #valueshsl = [[0.0 for a in range(3)] for b in range(100)]
    for a,b,c in coords:
        for x in range(10):
            for y in range(10):
                outp = [0,0,0,0,0,0,c]
                outp[0],outp[1],outp[2] = pix[(x+a), (y+b)]
                outp[0] = outp[0]/255
                outp[1] = outp[1]/255
                outp[2] = outp[2]/255
                outp[3],outp[4],outp[5] = colorsys.rgb_to_hls(outp[0],outp[1],outp[2])
                outp[3] = outp[3]/360
                outp[4] = outp[4]/100
                outp[5] = outp[5]/100
                result.append(outp)
    
    return result
    