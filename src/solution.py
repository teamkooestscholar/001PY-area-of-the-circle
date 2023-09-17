def calculate_circle_area(rad, dec=2):
    if rad < 0:
        raise ValueError("Radius cannot be negative.")
    
#   formula  
    area = 3.14159 * (rad ** 2)
    rounded_area = round(area, dec)
    return rounded_area

# input here
# dec for decimal so i live it at 2 decimal places
try:
    rad = float(14)
    dec = int(2)
    
    area = calculate_circle_area(rad, dec)
    print(f"The area of the circle with radius {rad} is: {area}")
except ValueError as e:
    print(f"Error: {e}")

#edit