from PIL import Image, ImageFilter, ImageDraw
from constants import *
import cv2
import colorsys
import numpy
from helpers import *

class CoinCategorize:
    def __init__(self, image, coins):
        self.image = image
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.rgb_pixels = self.image.load()
        self.coinSize = {}
        self.pennyIdx = [] # indexes of pennies
        self.nickelIdx = []
        self.dimeIdx = []
        self.quarterIdx = []
        self.coins = self.reformat_coins_and_find_pennies(coins)

    # now we take radius to be greater of rRadius or cRadius
    # coins is now object of form (rCenter, cCenter, radius, color)
    # also, see if there are any pennies, if so, 
    def reformat_coins_and_find_pennies(self, coins):
        for i in xrange(0, len(coins)):
            coins[i] = (coins[i][0], coins[i][1], max(coins[i][2], coins[i][3]), coins[i][4])
            if coins[i][3] == RED_RGB:    
                self.pennyIdx.append(i)
        return coins

    def get_coin_type_from_radius(self):
        if len(self.pennyIdx) != 0:
            self.coinSize['p'] = self.get_average_coin_radius(self.pennyIdx)
            for i in xrange(0, len(self.coins)):
                if i not in self.pennyIdx:
                    self.categorize_coin_with_penny_size(self.coins[i][2], i)
            # use penny radius to figure out value of other coins based on radius ratio
            return
        else:
            return 
        # else, create bins for coins of similar size (some threshold)
            # if there is only one type, then return error
            # else
                # sort from largest to smallest
                # take ration of largest to all rest
                # see which ratio set is closest -> take that as largest coin value
                # use largest coin size to determine others
   
    def categorize_coin_with_penny_size(self, radius, idx):
        qRatioDiff = abs(P_RATIOS['q'] - radius/self.coinSize['p'])
        dRatioDiff = abs(P_RATIOS['d'] - radius/self.coinSize['p'])
        nRatioDiff = abs(P_RATIOS['n'] - radius/self.coinSize['p'])

        if qRatioDiff < dRatioDiff:
            if qRatioDiff < nRatioDiff:
                self.quarterIdx.append(idx)
            else:
                self.nickelIdx.append(idx)
        else:
            if dRatioDiff < nRatioDiff:
                self.dimeIdx.append(idx)
            else:
                self.nickelIdx.append(idx)
        return

    # idx is an index list (pennyIdx, etc)
    def get_average_coin_radius(self, idx):
        radius = 0
        for i in xrange(0, len(idx)):
            radius += self.coins[idx[i]][2]
        return radius / float(len(idx))

    def get_coin_amount(self):
        return 0.25 * len(self.quarterIdx) + 0.1 * len(self.dimeIdx) + 0.05 * len(self.nickelIdx) + 0.01 * len(self.pennyIdx)
    
    def amount(self):
        self.get_coin_type_from_radius()
        return self.get_coin_amount()