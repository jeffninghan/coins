from PIL import Image, ImageFilter, ImageDraw
from constants import *
import cv2
import colorsys
import numpy
from helpers import *

class CoinImage:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.rgb_pixels = self.image.load()
        self.hls_pixels = self.convert_image_rgb_to_hls()

    def convert_image_rgb_to_hls(self):
        hls_pixels = []
        for r in xrange(0, self.height):
            row = []
            for c in xrange(0, self.width):
                h, l, s = colorsys.rgb_to_hls(self.get_rgb_pixel(r, c)[0]/255., self.get_rgb_pixel(r, c)[1]/255., self.get_rgb_pixel(r, c)[2]/255.)
                row.append((int(h * HLS_SCALE), int(l * HLS_SCALE), int(s * HLS_SCALE)))
            hls_pixels.append(row)
        return hls_pixels

    def preprocess_image(self):
        self.preprocess_color_scheme()
        self.preprocess_color_smoothing()
        return

    def preprocess_color_scheme(self):
        # color background white, pennies red and other coins black
        for r in xrange(0, self.height):
            for c in xrange(0, self.width):
                if (close_color(self.get_hls_pixel(r, c), WHITE_HLS, WHITE_HLS_THRESHOLD)):
                    self.set_rgb_pixel(r, c, WHITE_RGB)
                    self.set_hls_pixel(r, c, WHITE_HLS)
                elif (close_color(self.get_hls_pixel(r, c), SILVER_HLS, SILVER_HLS_THRESHOLD)):
                    self.set_rgb_pixel(r, c, BLACK_RGB)
                    self.set_hls_pixel(r, c, BLACK_HLS)
                elif (close_color(self.get_hls_pixel(r, c), PENNY_HLS, PENNY_HLS_THRESHOLD)):
                    self.set_rgb_pixel(r, c, RED_RGB)
                    self.set_hls_pixel(r, c, RED_HLS)
                else:
                    self.set_rgb_pixel(r, c, GREEN_RGB)
                    self.set_hls_pixel(r, c, GREEN_HLS)
        return

    def preprocess_color_smoothing(self):
        # smooths out colors by setting all colors in window to be the most common in window (uses voting scheme)
        for r in xrange(0, self.height, SMOOTHING_RESOLUTION):
            for c in xrange(0, self.width, SMOOTHING_RESOLUTION):
                window = (r, min(r + SMOOTHING_RESOLUTION, self.height), c, min(c + SMOOTHING_RESOLUTION, self.width))
                color = self.most_common_color(window[0], window[1], window[2], window[3])
                self.set_window_color(window[0], window[1], window[2], window[3], color)
        return

    def most_common_color(self, r_min, r_max, c_min, c_max):
        # color choices are WHITE, BLACK, RED or GREEN
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
        return colors[max_vote_idx]

    def set_window_color(self, r_min, r_max, c_min, c_max, rgb):
        for r in xrange(r_min, r_max):
            for c in xrange(c_min, c_max):
                self.set_rgb_pixel(r, c, rgb)
                if rgb == WHITE_RGB:
                    self.set_hls_pixel(r, c, WHITE_HLS)
                elif rgb == BLACK_RGB:
                    self.set_hls_pixel(r, c, BLACK_HLS)
                elif rgb == RED_RGB:
                    self.set_hls_pixel(r, c, RED_HLS)
                else:
                    self.set_hls_pixel(r, c, GREEN_HLS)
        return

    def get_hls_pixel(self, row, col):
        assert(row < self.height and row >= 0)
        assert(col < self.width and col >= 0)
        return self.hls_pixels[row][col]

    def get_rgb_pixel(self, row, col):
        assert(row < self.height and row >= 0)
        assert(col < self.width and col >= 0)
        return self.rgb_pixels[col, row]

    def set_hls_pixel(self, row, col, hls):
        assert(row < self.height and row >= 0)
        assert(col < self.width and col >= 0)
        self.hls_pixels[row][col] = hls

    def set_rgb_pixel(self, row, col, rgb):
        assert(row < self.height and row >= 0)
        assert(col < self.width and col >= 0)
        self.rgb_pixels[col, row] = rgb

    def process(self):
        self.preprocess_image()
        self.image.save('img/preprocessed.jpg', 'JPEG')
        return self.image