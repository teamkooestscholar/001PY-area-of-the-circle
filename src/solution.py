# 001 Write a function that calculates the area of a circle by a given radius.
def calculate_circle_area(radius):

    assert radius > 0
    total = 3.141559*(radius**2)
    return total

num = float(input("Enter the radius of the circle: "))
print("The area of the circle is --> ", round(calculate_circle_area(num),3))


