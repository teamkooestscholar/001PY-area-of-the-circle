import math

def calculate_circle_area(radius, decimal_places=2):
    if radius < 0:
        return "Error: Radius cannot be negative"
    else:
        area = math.pi * (radius ** 2)
        rounded_area = round(area, decimal_places)
        return rounded_area

# Example usage with assert statement:
radius = float(input("Enter the radius of the circle: "))
decimal_places = int(input("Enter the number of decimal places for rounding: "))

result = calculate_circle_area(radius, decimal_places)
print(f"The area of the circle with radius {radius} is approximately {result}")