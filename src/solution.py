import math

def calculate_circle_area(radius, decimal_places=None):
    try:
        assert radius >= 0, "Radius cannot be negative"
        area = math.pi * (radius ** 2)
        if decimal_places is not None:
            area = round(area, decimal_places)
        return area
    except AssertionError as e:
        return str(e)

# Bonus Challenge 1
print(calculate_circle_area(-5))
print(calculate_circle_area(5))

# Bonus Challenge 2:
if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        decimal_places = int(input("Enter the number of decimal places (or press Enter for no rounding): "))
        result = calculate_circle_area(radius, decimal_places)
        print(f"The area of the circle is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius and decimal places.")

# Bonus Challenge 3
print(calculate_circle_area(5, 2))