#function that calculates area of circle

def calculate_circle_area(radius):
    assert radius > 0,"Error: radius should be positive" 
    return round(3.14159 * pow(radius, 2), 2)

value = int(input("Enter radius: "))
print(calculate_circle_area(value))