# # Write a function that calculates the area of a circle by a given radius.
# def calculate_circle_area(_):
#     pass

import math

def calculate_circle_area(radius, decimal_places=2):
    try:
        assert radius >= 0, "Radius cannot be negative"
        area = math.pi * radius ** 2
        rounded_area = round(area, decimal_places)
        return rounded_area
    except AssertionError as e:
        return str(e)

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    decimal_places = int(input("Enter the number of decimal places for rounding: "))

    area = calculate_circle_area(radius, decimal_places)

    if isinstance(area, float):
        print(f"The area of the circle with radius {radius} is: {area}")
    else:
        print(area)
