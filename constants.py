# File of coin sizes and constants
# 'P' -> penny, 'N' -> nickel 'D' -> dime, 'Q' -> quarter
# absolute coin sizes according to US treasury
P_SIZE = 19.05 # in millimeters
N_SIZE = 21.21
D_SIZE = 17.91 # this means DIME SIZE, geez don't be so immature ;0
Q_SIZE = 24.26

# ratio of coin sizes to all other coins
P_RATIOS = { 'n': 1.11, # ratio of {nickel, dime, quarter}/penny
             'd': 0.94, 
             'q': 1.27 }
N_RATIOS = { 'p': 0.90, 
             'd': 0.84, 
             'q': 1.14 }
D_RATIOS = { 'p': 1.06, 
             'n': 1.18, 
             'q': 1.35 }
Q_RATIOS = { 'p': 0.79, 
             'n': 0.87, 
             'd': 0.74 }

# Resolution for coin coloring in (pixels)
SMOOTHING_RESOLUTION = 4

# Minimum coin diameter
MIN_COIN_DIAMETER = 10

# Window for color determination (pixels used to vote with)
COLOR_WINDOW = 3

# Threshold for coloring picture area white or black
THRESHOLD = 50

IMG_FILE ='img/penny_nickel_dime_quarter.jpg' #'img/test_circles.jpg' #

WHITE_RGB = (255, 255, 255)
BLACK_RGB = (0, 0, 0)
RED_RGB = (255, 0, 0)
GREEN_RGB = (0, 255, 0)

HLS_SCALE = 240
WHITE_RGB_THRESHOLD = (10, 10, 10)
BLACK_RGB_THRESHOLD = (10, 10, 10)

# hue should be within 24 of this; l, s can be anything
PENNY_HLS = (12, 100, 100)
PENNY_HLS_THRESHOLD = (12, HLS_SCALE, HLS_SCALE)

# saturation should be below 50, luminescence should be below 160
SILVER_HLS = (45, 80, 25)
SILVER_HLS_THRESHOLD = (HLS_SCALE, 80, 25)

# luminscence needs to be above 160; h, s can be anything
WHITE_HLS = (160, 240, 0)
WHITE_HLS_THRESHOLD = (HLS_SCALE, 40, HLS_SCALE)

BLACK_HLS = (160, 0, 0)
RED_HLS = (0, 120, 240)
GREEN_HLS = (80, 120, 240)