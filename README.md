coins
=====

Detects coins from a given image and outputs their summed value. Requires various python modules such as numpy, OpenCV, PIL.

Assumptions
=====
There are at least two types of coins in the image. This is needed to figure out the relative sizes of each coin which in turn is used to categorized which coin it is.
For now, assume that background color is white (put coins on a piece of printer paper).
None of the coins are overlapping or stacked on top of each other.
Coins have diameter of at least MIN_COIN_DIAMETER
Only pennies, nickels, dimes, and quarters are supported

Classes
=====
CoinImage
This class describes an imported coin image. This class does the following:
1) Determines the background color of the image (not implemented yet).
2) Goes through image and colors non-penny coins black, pennies red and background white.


CoinCategorize
This class provides all the functionality to determine what coins are in an image. There are two steps for this:
1) Determine the radius and center of each circle in the image.
2) Also distinguishes pennies from other coins based on the color
3) Determines how many of each coin exists on the image
4) Returns the total value of the coins.