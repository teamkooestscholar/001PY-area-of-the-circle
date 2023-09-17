
# Modify the function to handle negative radii gracefully and return an error message. (Hint: use the assert statement) [+5 extra credit points]
#
# Create a Python script that prompts the user to input a radius and then displays the calculated area. (Hint: use the input function) [+5 extra credit points]
#
# Enhance the function to round the calculated area to a specified number of decimal places. (Hint: use the round function) [+5 extra credit points
#


#add co author

try:

    r = float(input("Enter the Radius value"))


    assert r >= 0, "Radius must be non-negative"

    decimal_place = int(input("Enter the number of decimal places for rounding: " ))

    area = round(3.14159265359 * r ** 2, decimal_place)

    print("The area of the circle is ", area)
except ValueError:
    print("Input is invalid Please enter a valid number next time ")