from PIL import Image, ImageFilter
import cv2
import cv2.cv as cv
import numpy as np
import sys
import constants
import helpers
from coin_image import CoinImage
from coin_find import CoinFind
from coin_categorize import CoinCategorize
# img = cv2.imread('img/test_circles.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('detected circles',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# circ = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 5, 50)
# print circ
# file = "penny_nickel_dime_quarter.jpg"

# def main(file):
#     # img = Image.open(file)
#     # #out = img.resize( [int(0.1 * s) for s in img.size] )
#     # #out.save('resized.jpg', 'JPEG')
#     # (width, height) = img.size
#     #edged = img.filter(ImageFilter.FIND_EDGES)
#     #px = colorWhiteOrBlack(edged.load(), width, height) # coins are white, background is black
#     #edged.save('coloredWhite.jpg', 'JPEG')
    
#     img = cv2.imread(file)
#     output = img.copy()
#     gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     #for i in range(0, len(img)):
#         #for j in range(0, len(img[i])):
#             #if img[i, j] < 170:
#                 #img[i, j] = 0
#             #else:
#                 #img[i, j] = 255

#     # cimg = cv2.medianBlur(img,5)
#     # cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)  
#     circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 2.5, 10)
#     print circles
#     if len(circles):
#         circles = np.uint16(np.around(circles))
#         for i in circles[0,:]:
#             # draw the outer circle
#             cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
#             # draw the center of the circle
#             cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)
    
#         cv2.imshow('detected circles',output)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()    
#     return
    
# def colorWhiteOrBlack(px, width, height):
#     for i in xrange(0, width, constants.RES):
#         for j in xrange(0, height, constants.RES):
#             px = helpers.threshold(px, i, min(i + constants.RES, width), j, min(j + constants.RES, height), constants.THRESHOLD)
#     return px
    
# def removeBlackEdge(px, width, height):
#     px = helpers.colorRange(px, 0, width, 0, constants.RES, 'white')
#     px = helpers.colorRange(px, 0, constants.RES, 0, height, 'white')
#     return px

# def main(file):
#     img = Image.open(file)
#     (width, height) = img.size
#     edges = img.filter(ImageFilter.FIND_EDGES)
#     edges.save('img/edges.jpg', 'JPEG')
#     edges = edges.filter(ImageFilter.FIND_EDGES)
#     edges.save('img/edges.jpg', 'JPEG')
#     px = colorWhiteOrBlack(edges.load(), width, height)
#     px = removeBlackEdge(px, width, height)
#     edges.save('img/coloredWhite.jpg', 'JPEG')

#     # px2 = colorWhiteOrBlack(px, width, height)
#     # px2.save('img/2.jpg', 'JPEG')
#     img = cv2.imread('img/coloredWhite.jpg', 0)
#     print img
#     cimg = cv2.medianBlur(img,5)
#     cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#     circles = cv2.HoughCircles(img, cv.CV_HOUGH_GRADIENT,2,50,param1=10,param2=50,minRadius=10,maxRadius=150)
#     print circles
#     if len(circles):
#         circles = np.uint16(np.around(circles))
#         for i in circles[0,:]:
#             # draw the outer circle
#             cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#             # draw the center of the circle
#             cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
#         cv2.imshow('detected circles',cimg)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()    
#     return

# main(constants.IMG_FILE)

filename = 'img/pndq.jpg'
def main(filename):
    coinImage = CoinImage(filename)
    # returns an PIL image object
    processedImage = coinImage.process()

    coinFind = CoinFind(processedImage)
    coinFind.find()
    coinCategorize = CoinCategorize(coinFind.image, coinFind.coins)
    print coinCategorize.amount()

main(filename)