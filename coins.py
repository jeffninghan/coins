from PIL import Image, ImageFilter
import cv2
import cv2.cv as cv
import numpy as np
import constants
import helpers

file = "penny_nickel_dime_quarter.jpg"
def main(file):
    img = Image.open(file)
    #out = img.resize( [int(0.1 * s) for s in img.size] )
    #out.save('resized.jpg', 'JPEG')
    (width, height) = img.size
    #edged = img.filter(ImageFilter.FIND_EDGES)
    #px = colorWhiteOrBlack(edged.load(), width, height) # coins are white, background is black
    #edged.save('coloredWhite.jpg', 'JPEG')
    
    img = cv2.imread(file, 0)
    cimg = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    
    circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,100,param1=10,param2=50,minRadius=30,maxRadius=100)
    print circles
    if len(circles):
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
        cv2.imshow('detected circles',cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()    
    return
    
def colorWhiteOrBlack(px, width, height):
    for i in xrange(0, width, constants.RES):
        for j in xrange(0, height, constants.RES):
            px = helpers.threshold(px, i, min(i + constants.RES, width), j, min(j + constants.RES, height), constants.THRESHOLD)
    return px
    
main(file)