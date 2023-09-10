import math

def calculate_circle_area(radius, decimal_places=2):
   
    assert radius >= 0, "Radius cannot be negative"
    area = math.pi * radius**2
    return round(area, decimal_places)

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
