from PIL import Image, ImageFilter, ImageDraw
from constants import *
import cv2
import numpy
from helpers import *

class CoinFind:
    def __init__(self, processedImage):
        self.image = processedImage
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.rgb_pixels = self.image.load()
        # circle object of form (rCenter, cCenter, rRadius, cRadius, color) color [RED_RGB, BLACK_RGB]
        # we have radius for row and column dimensions because objects may not be perfectly circular
        self.coins = []

    def get_coin_from_internal_point(self, row, col):
        # make sure point is inside a circle
        assert(self.within_coin(row, col))
        # find vertical cord through circle
        rTop = None
        rBottom = None
        r = row
        c = col
        while r >= 0:
            if self.reached_edge(r, c):
                rTop = r
                break
            else:
                r -= 1
        r = row
        while r < self.height:
            if self.reached_edge(r, c):
                rBottom = r
                break
            else:
                r += 1
        if rTop == None:
            rTop = 0
        if rBottom == None:
            rBottom = self.height
        rCenter = (rTop + rBottom) / 2

        # find horizontal diameter line of circle
        cLeft = None
        cRight = None
        c = col
        while c >= 0:
            if self.reached_edge(rCenter, c):
                cLeft = c
                break
            else:
                c -= 1
        c = col
        while c < self.width:
            if self.reached_edge(rCenter, c):
                cRight = c
                break
            else:
                c += 1
        if cLeft == None:
            cLeft = 0
        if cRight == None:
            cRight = self.width   
        cCenter = (cLeft + cRight) / 2

        cRadius = (abs(cCenter - cLeft) + abs(cRight - cCenter)) / 2
        rRadius = (abs(rCenter - rTop) + abs(rBottom - rCenter)) / 2
        radius = max(cRadius, rRadius)

        return (rCenter, cCenter, rRadius, cRadius)

    def find_all_coins(self):
        for r in xrange(0, self.height, MIN_COIN_DIAMETER):
            for c in xrange(0, self.width, MIN_COIN_DIAMETER):
                if self.within_coin(r, c) and self.not_within_found_coin(r, c):
                    rCenter, cCenter, rRadius, cRadius = self.get_coin_from_internal_point(r, c)
                    color = self.get_color_for_coin(rCenter, cCenter)
                    if color is not None:
                        self.coins.append((rCenter, cCenter, rRadius, cRadius, color))
                    else:
                        print 'color of coin is neither red or black, not appending to coin list'
        self.remove_close_centers()
        return

    def reached_edge(self, row, col):
        if self.get_rgb_pixel(row, col) == WHITE_RGB or self.get_rgb_pixel(row, col) == GREEN_RGB:
            return True
        return False

    def within_coin(self, row, col):
        if self.get_rgb_pixel(row, col) == BLACK_RGB or self.get_rgb_pixel(row, col) == RED_RGB:
            return True
        return False 

    def not_within_found_coin(self, row, col):
        # remember coin is of form: (rCenter, cCenter, rRadius, cRadius, color)
        # we model coins as ellipses for better accuracy
        for coin in self.coins:
            val = (row - coin[0])**2/float(coin[2])**2 + (col - coin[1])**2/float(coin[3])**2
            if val <= 1:
                return False
        return True

    def get_color_for_coin(self, rCenter, cCenter):
        # use voting scheme to get color
        r_min = max(rCenter - COLOR_WINDOW, 0)
        r_max = min(rCenter + COLOR_WINDOW, self.height)
        c_min = max(cCenter - COLOR_WINDOW, 0)
        c_max = min(cCenter + COLOR_WINDOW, self.width)

        colors = [WHITE_RGB, BLACK_RGB, RED_RGB, GREEN_RGB]
        votes = [0, 0, 0, 0]
        for r in xrange(r_min, r_max):
            for c in xrange(c_min, c_max):
                if self.get_rgb_pixel(r, c) == WHITE_RGB:
                    votes[0] += 1
                elif self.get_rgb_pixel(r, c) == BLACK_RGB:
                    votes[1] += 1
                elif self.get_rgb_pixel(r, c) == RED_RGB:
                    votes[2] += 1
                else:
                    votes[3] += 1
        max_vote_idx = 0
        max_vote = 0
        for i in xrange(0, len(votes)):
            if votes[i] > max_vote:
                max_vote_idx = i
                max_vote = votes[i]
        if colors[max_vote_idx] == WHITE_RGB or colors[max_vote_idx] == GREEN_RGB:
            return None
        return colors[max_vote_idx]

    def remove_close_centers(self):
        # remove centers that are too close togther
        # find list of coins indexes that have centers that are too close
        coin_idx_to_remove = []
        for i in xrange(0, len(self.coins)):
            for j in xrange(i, len(self.coins)):
                # if one center is within another's radius, then they are too close
                min_i_radius = max(self.coins[i][2], self.coins[i][3])
                min_j_radius = max(self.coins[j][2], self.coins[j][3])
                if i != j and self.distance(self.coins[i], self.coins[j]) < max(min_i_radius, min_j_radius):
                    if min_i_radius > min_j_radius:
                        coin_idx_to_remove.append(j)
                    else:
                        coin_idx_to_remove.append(i)
        # create new list of coins that are not too close to each other
        coins = []
        for i in xrange(0, len(self.coins)):
            if i not in coin_idx_to_remove:
                coins.append(self.coins[i])

        self.coins = coins
        return

    def distance(self, coin1, coin2):
        return ((coin1[0] - coin2[0])**2 + (coin1[1] - coin2[1])**2)**0.5

    def get_rgb_pixel(self, row, col):
        assert(row < self.height and row >= 0)
        assert(col < self.width and col >= 0)
        return self.rgb_pixels[col, row]

    def set_rgb_pixel(self, row, col, rgb):
        assert(row < self.height and row >= 0)
        assert(col < self.width and col >= 0)
        self.rgb_pixels[col, row] = rgb

    def draw_radii(self):
        draw = ImageDraw.Draw(self.image)
        for coin in self.coins:
            cLeft = coin[1] - coin[3]
            rCenter = coin[0]
            cCenter = coin[1]
            # draw.point((cCenter, rCenter), 'red')
            draw.line((cLeft, rCenter, cCenter, rCenter), 'yellow')
        self.image.save('img/circle_detected.jpg')

    def find(self):
        self.find_all_coins()
        self.draw_radii()
        return

# filename = 'img/coloredWhite.jpg'
# image = Image.open(filename)
# categorize = CoinCategorize(image)
# categorize.find()
# print categorize.coins