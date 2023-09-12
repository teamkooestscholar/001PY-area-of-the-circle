import math

def calculate_circle_area(radius, decimal_places=2):
    assert radius > 0, "Error: Negative or zero radius is not allowed."
    area = math.pi * (radius ** 2)
    return round(area, decimal_places)

try:
    radius = float(input("Enter the radius of a circle: "))
    decimal_places = int(input("Enter the number of decimal places (default is 2): "))
    print("The area is -->", calculate_circle_area(radius, decimal_places))
except ValueError:
    print("Invalid input. Please enter a valid value for the radius.")
except AssertionError as e:
    print(e)
