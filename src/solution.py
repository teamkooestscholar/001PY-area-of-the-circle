# Write a function that calculates the area of a circle by a given radius.
def calculate_circle_area(radius,decimal_places=2):
    assert radius > 0
    total = 3.141559*(radius**2)
    
    return round(total,decimal_places)


try:
    num = float(input("Enter the radius of a circle: "))
    decimal_places = int(input("Enter the number of decimal places (default is 2): "))
    print("The area is --> ", calculate_circle_area(num, decimal_places))
except ValueError:
    print("Invalid input. Please enter a valid value for the radius.")
except AssertionError:
    print("Error: Negative or zero radius is not allowed.")



