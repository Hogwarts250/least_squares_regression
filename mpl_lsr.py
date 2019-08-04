import math
import numpy as np
import matplotlib.pyplot as plt

def graph_slope_intercept(slope, y_intercept, lowest_x, greatest_x):
    x = np.array(range(math.floor(lowest_x), math.ceil(greatest_x) + 1))
    y = slope * x + y_intercept

    plt.plot(x, y)

def plot_coordinates(cartesian_coordinates, slope, y_intercept):
    x_coordinates = []
    y_coordinates = []
    greatest_x = 0
    lowest_x = 0

    for coordinate in cartesian_coordinates:
        if coordinate[0] > greatest_x:
            greatest_x = coordinate[0]

        elif coordinate[0] < lowest_x:
            lowest_x = coordinate[0]

        x_coordinates.append(coordinate[0])
        y_coordinates.append(coordinate[1])

    plt.scatter(x_coordinates, y_coordinates)
    graph_slope_intercept(slope, y_intercept, lowest_x, greatest_x)
    plt.grid(b = True, linestyle = "dashed")

    plt.title("Line of Best Fit", fontsize = 18)
    plt.xlabel("x")
    plt.ylabel("y")
    
    plt.savefig("lsr.png", bbox_inches = "tight")