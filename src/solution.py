# Write a function that calculates the area of a circle by a given radius.
import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = math.pi * (radius ** 2)
        return area

# Example usages:
radius1 = 5.0
radius2 = 2.5
radius3 = 0
radius4 = -3.0

area1 = calculate_circle_area(radius1)
area2 = calculate_circle_area(radius2)
area3 = calculate_circle_area(radius3)
area4 = calculate_circle_area(radius4)

print(f"The area of a circle with radius {radius1} is {area1:.2f}")
print(f"The area of a circle with radius {radius2} is {area2:.2f}")
print(f"The area of a circle with radius {radius3} is {area3:.2f}")
print(f"The area of a circle with radius {radius4} is {area4}")

  