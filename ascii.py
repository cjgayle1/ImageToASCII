import imageio.v2 as io
import numpy as np
import cv2

MAX_RGB = 255
SCALE = 100
DEFAULT_NAME = "rio.jpg"
IMAGE_NAME = input("Please type the name of the image you would like to convert: ")


# check image and use default if it doesnt exist
try:
    img = io.imread(IMAGE_NAME)
except:
    print("Couldn't find that image.")
    img = io.imread(DEFAULT_NAME)

# resize so that it can be more easily seen in console
img = cv2.resize(img, ((int(img.shape[1] / (img.shape[0] / SCALE))), SCALE))

# brightness array
bgw = np.empty((img.shape[0], img.shape[1]))

# result array
res = []

# get each pixels brightness value 
for i in range(len(img)):
    for j in range(len(img[i])):
        pixel = img[i][j]
        bgw[i][j] = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) // 3
        
# ascii values from least bright to brightest
ascii = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
        'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
        'a','o','*','#','M','W','&','8','%','B','@','$']

ascii_bgw = {}

# increment amount for each range of values
inc_range = MAX_RGB // len(ascii)

# current increment value
cur_inc = 0

# sets up each range
for val in ascii:
    ascii_bgw[(cur_inc, cur_inc + inc_range)] = val
    cur_inc += inc_range + 1

# match each value to the proper range
for i in range(len(bgw)):
    temp = []
    for j in range(len(bgw[i])):
        cur_inc = bgw[i][j]
        for floor, ceil in ascii_bgw.keys():
            if floor <= cur_inc <= ceil:
                temp.append(ascii_bgw[(floor, ceil)])
                break
    res.append(temp)

# formats it nicely
for i in res:
    pr = [j * 3 for j in i]
    print("".join(pr))