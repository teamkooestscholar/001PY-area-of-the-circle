# Write a function that calculates the area of a circle by a given radius.
def calculate_circle_area(radius, decimal_places=2):
    assert radius >= 0, "Input must not be negative."
    area = 3.14159 * (radius ** 2)
    return round(area, decimal_places)

try:
    radius = float(input("Enter the radius of the circle: "))
    decimal_places = int(input("Enter the number of decimal places for rounding: "))
    area = calculate_circle_area(radius, decimal_places)
    print(f"The rounded area of the circle with radius {radius} is: {area}")
except AssertionError as e:
    print("Error:", e)


