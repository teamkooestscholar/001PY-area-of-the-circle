import math
# Write a function that calculates the area of a circle by a given radius.
def calculate_circle_area(radius, decimal_places=2):
    try:
        assert radius >= 0, "Oops! Radius can't be negative."
        area = math.pi * (radius ** 2)
        return round(area, decimal_places)
    except AssertionError as e:
        return str(e)

def main():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            decimal_places = int(input("Enter the number of decimal places: "))
            area = calculate_circle_area(radius, decimal_places)
            if isinstance(area, str):
                print(area)
            else:
                print(f"The area of the circle is: {area}")
            break  
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()