import math

def calculate_circle_area(radius):
    """ Calculate and return the area of a circle. """
    try:
        assert radius >= 0, "Radius must be non-negative"
        area = math.pi * (radius ** 2)
        return area
    except AssertionError as e:
        return str(e)

def main():
    print("Welcome to the Circle Area Calculator!")

    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()