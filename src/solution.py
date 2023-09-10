def calculate_circle_area(radius, decimal_places=2):
    try:
        # Bonus Challenge 1: Handle negative radii gracefully
        assert radius >= 0, "THE RADIUS SHOULD BE POSITIVE."
        area = 3.14159 * (radius ** 2)
        # Bonus Challenge 3: Round the calculated area to the specified number of decimal places
        rounded_area = round(area, decimal_places)
        return rounded_area
    except AssertionError as e:
        # Bonus Challenge 1: Raise the error for negative radii
        raise ValueError(str(e))

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        decimal_places = int(input("Enter the number of decimal places for rounding: "))
        area = calculate_circle_area(radius, decimal_places)
        print(f"The area of the circle is: {area}")
    except ValueError as e:
        # Bonus Challenge 2: Handle invalid input gracefully
        print(f"Error: {e}")
        
        
     #test   
    #Enter the radius of the circle: 3
    #Enter the number of decimal places for rounding: 4
    #The area of the circle is: 28.2743
    
    #Enter the radius of the circle: -8
    #Enter the number of decimal places for rounding: 32
    #ERROR!
    #Error: THE RADIUS SHOULD BE POSITIVE.
