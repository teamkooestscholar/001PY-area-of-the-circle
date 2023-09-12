def calculate_circle_area(radius, decimal_places=2):
    if radius < 0:
        return "Error: Radius cannot be negative."
    
    area = 3.14159 * (radius ** 2)
    return round(area, decimal_places)

try:
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    if isinstance(area, str):
        print(area)  
    else:
        print(f"The area of the circle with radius {radius} is  {area}")
except ValueError:
    print("Invalid input enter a valid number for the radius.")