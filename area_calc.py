import math


def print_calc(height, width, cover):

    area = height * width
    num_of_cans = math.ceil(area/cover)
    print(f"The number of cans that can paint {height}m and {width}m width is {num_of_cans}")


test_h = int(input("Enter the height of the wall:\n"))
test_w = int(input("Enter the width of the wall: \n"))
coverage = 5
print_calc(height=test_h, width=test_w, cover=coverage)
