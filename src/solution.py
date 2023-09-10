import math

def calculate_circle_area(radius, decimal_places=2):
    try:
        # Check if the radius is non-negative
        assert radius >= 0, "Radius must be a non-negative number."

        # Calculate the area of the circle using the formula: A = π * r^2
        area = math.pi * (radius ** 2)

        # Round the area to the specified number of decimal places
        rounded_area = round(area, decimal_places)

        return rounded_area
    except AssertionError as e:
        return str(e)
    except ValueError:
        return "Invalid input. Please enter a valid numeric value for the radius."

def main():
    try:
        # Get the radius from the user
        radius = float(input("Enter the radius of the circle: "))
        
        # Get the number of decimal places from the user
        decimal_places = int(input("Enter the number of decimal places to round to (default is 2): ") or 2)
        
        # Calculate the area and display the result
        circle_area = calculate_circle_area(radius, decimal_places)
        print(f"The area of the circle is: {circle_area}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except EOFError:
        print("\nProgram terminated by user (EOF).")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
