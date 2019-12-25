from least_squares_regression import calc_lsr, calc_stnd_deviation
import ast

while True:
    print("Input your coordinates in this format: (x1, y1), (x2, y2) (x3, y3)")
    input_coordinates = ast.literal_eval(input())

    m, b = calc_lsr(input_coordinates)
    print("\nslope = " + str(m), "\ny-intercept = " + str(b), "\ny = " + str(m) + "x + " + str(b))

    stnd_deviation = calc_stnd_deviation(m, b, input_coordinates)
    print("standard deviation = " + str(stnd_deviation))

    if input("\nDo you need to find another line of best fit? (y/n) ") == "n":
        break