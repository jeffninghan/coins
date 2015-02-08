# File of helper functions for detecting coins

# def threshold(px, x_min, x_max, y_min, y_max, thresh):
#     px_sum = 0
#     color = (255, 255, 255)
#     for i in range(x_min, x_max):
#         for j in range(y_min, y_max):
#             px_sum = px_sum + sum(list(px[i, j]))
#     px_average = px_sum / ( 3 * max((x_max-x_min-1), 1) * max((y_max-y_min-1), 1))
#     if px_average > thresh:
#         color = (0, 0, 0) # color everything black
#     for i in range(x_min, x_max):
#         for j in range(y_min, y_max):
#             px[i, j] = color
#     return px

# def colorRange(px, x_min, x_max, y_min, y_max, c):
#     if c == 'white':
#         color = (255, 255, 255)
#     else:
#         color = (0, 0, 0)

#     for i in range(x_min, x_max):
#         for j in range(y_min, y_max):
#             px[i, j] = color
#     return px

# Determines if one color is close (within threshold) to another
# c1 and c2 are rgb value of form (r, g, b), threshold is also of form (r, g, b), the max distance away corresponding rgb values can be from each other
def close_color(c1, c2, threshold):
    if (abs(c1[0] - c2[0]) > threshold[0]):
        return False
    if (abs(c1[1] - c2[1]) > threshold[1]):
        return False
    if (abs(c1[2] - c2[2]) > threshold[2]):
        return False
    return True