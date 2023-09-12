# Write a function that calculates the area of a circle by a given radius.

def calculate_circle_area(radius):
    assert radius >= 0, "Radius must be non-negative"
    area = 3.14159 * (radius ** 2)
    return round(area, 2)

radius = float(input("Enter desired radius: "))

try:
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area}")
except AssertionError as e:
    print(e)

