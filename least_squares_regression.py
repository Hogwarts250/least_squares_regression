import ast

def literal_input():
    try: 
        cartesian_coordinates = ast.literal_eval(input())

    except:
        literal_input()
     
    return cartesian_coordinates

def calc_lsr(cartesian_coordinates):
    n = len(cartesian_coordinates)

    x, y, x2, xy = 0, 0, 0, 0

    for coordinate in cartesian_coordinates:
        x += coordinate[0]
        y += coordinate[1]
        x2 += coordinate[0] ** 2
        xy += coordinate[0] * coordinate [1]
    
    m = (n * xy - x * y) / (n * x2 - x ** 2)
    b = (y - m * x) / n
    
    return m, b

def calc_stnd_deviation(slope_intercept, cartesian_coordinates):
    total_deviation = 0

    for coordinate in cartesian_coordinates:

        y = slope_intercept[0] * coordinate[0] + slope_intercept[1]
        deviation = abs(coordinate[1] - y)

        total_deviation += deviation
    
    return total_deviation / len(cartesian_coordinates)

while True:
    print("Input you coordinates in this format: (x1, y1), (x2, y2) (x3, y3)")
    input_coordinates = literal_input()

    m, b = calc_lsr(input_coordinates)
    print("\nslope = " + str(m), "\ny-intercept = " + str(b), "\ny = " + str(m) + "x + " + str(b))

    stnd_deviation = calc_stnd_deviation(calc_lsr(input_coordinates), input_coordinates)
    print("standard deviation = " + str(stnd_deviation))

    if input("\nDo you need to find another line of best fit? (y/n) ") == "n":
        break