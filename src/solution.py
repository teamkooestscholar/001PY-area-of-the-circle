# Write a function that calculates the area of a circle by a given radius.

def calculate_circle_area(radius):
    return 3.14159 * (radius ** 2)

radius = float(input("Enter desired radius: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}")

