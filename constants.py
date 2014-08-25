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
RES = 4

# Threshold for coloring picture area white or black
THRESHOLD = 75
