import cv2
import os
from random import randint

command = "pubg"
type = "file"

def process(args,client):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    image = cv2.imread(dir_path + "\\map_map.png")
    print(dir_path + "\\map_map.png")
    height, width, channels = image.shape
    r = 255
    g = 255
    b = 255
    while(r == 255 and g == 255 and b == 255):
        row = randint(0, height-1)
        col = randint(0, width-1)
        r = image[col][row][0]
        g = image[col][row][1]
        b = image[col][row][2]
           
    mapImage = cv2.imread(dir_path + "\\map3.jpg")
    cv2.circle(mapImage, (row, col), 30, (0,0,255), 4)
    cv2.imwrite(dir_path + "\\tempMap.jpg",mapImage)
    return dir_path + "\\tempMap.jpg" 