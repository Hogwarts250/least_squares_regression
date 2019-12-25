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

def calc_stnd_deviation(slope, y_intercept, cartesian_coordinates):
    total_deviation = 0

    for coordinate in cartesian_coordinates:

        y = slope * coordinate[0] + y_intercept
        deviation = abs(coordinate[1] - y)

        total_deviation += deviation
    
    stnd_deviation = total_deviation / len(cartesian_coordinates)

    return stnd_deviation