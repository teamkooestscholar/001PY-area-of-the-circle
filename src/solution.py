import math

def calculate_circle_area(radius, decimal_places=None):
    try:
        assert radius >= 0, "Radius must be non-negative."

        area = math.pi * (radius ** 2)

        if decimal_places is not None:
            area = round(area, decimal_places)

        return area
    except AssertionError as e:
        return str(e)

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        decimal_places = int(input("Enter the number of decimal places to round to: "))
        
        result = calculate_circle_area(radius, decimal_places)
        
        if isinstance(result, str):
            print(f"Error: {result}")
        else:
            print(f"The area of the circle is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric radius.")

if __name__ == "__main__":
    main()
