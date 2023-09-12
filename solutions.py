import math

def calculate_circle_area(radius, decimal_places=2):
    assert radius >= 0, "Radius cannot be negative"
    
    area = math.pi * radius**2
    return round(area, decimal_places)

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        decimal_places = int(input("Enter the number of decimal places for the result (default is 2): ") or 2)

        area = calculate_circle_area(radius, decimal_places)
        print(f"The area of the circle with radius {radius} is {area}")
    
    except ValueError:
        print("Invalid input. Please enter a valid radius value.")
    except AssertionError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()