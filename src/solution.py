import math

def circle_area(radius, decimals=2):
    try:
        assert radius >= 0
        area = round(math.pi * radius ** 2, decimals)
        return f"Area: {area}"
    except AssertionError:
        return "Error: Radius must be non-negative."

try:
    r = float(input("Enter radius: "))
    d = int(input("Enter decimals (default is 2): ")) or 2
    print(circle_area(r, d))
except ValueError:
    print("Invalid input. Please enter a valid number for the radius and decimals.")
