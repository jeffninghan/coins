# File of helper functions for detecting coins

def threshold(px, x_min, x_max, y_min, y_max, thresh):
    px_sum = 0
    color = (255, 255, 255)
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            px_sum = px_sum + sum(list(px[i, j]))
    px_average = px_sum / ( 3 * max((x_max-x_min-1), 1) * max((y_max-y_min-1), 1))
    if px_average > thresh:
        color = (0, 0, 0) # color everything white
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            px[i, j] = color
    return px
