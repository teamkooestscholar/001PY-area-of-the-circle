import math
def calculate_circle_area():
    radius = float(input("Enter Desired Radius: "))
    
    if radius < 0:
        return "Error: Radius cannot be negative."
    
    area = math.pi * (radius ** 2)
    rounded_area = round(area, 2)
    return rounded_area

area = calculate_circle_area()
if isinstance(area, str):
    print(area)
else:
    print(f"The area is {area}.")