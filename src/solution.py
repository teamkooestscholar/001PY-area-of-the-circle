# Write a function that calculates the area of a circle by a given radius.
import math

def calculate_circle_area(radius):
    assert radius > 0
    area = math.pi * (radius ** 2)
    return area

num = float(input("Enter the radius of a circle: "))
print("The area is ", round(calculate_circle_area(num), 3))

