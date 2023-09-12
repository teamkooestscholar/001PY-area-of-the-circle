# Calculate the Area of a Circle

This Python program calculates the area of a circle based on a user-provided radius while incorporating error handling to ensure that the radius is non-negative.

## Function for Calculation

The code defines a function `calculate_circle_area` for calculating the area of the circle with proper error handling. The function uses the formula `π * radius^2` for the calculation.

```python
def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    :raise AssertionError: If the radius is negative.
    """
    assert radius >= 0, "Radius must be non-negative"
    area = 3.14159 * (radius ** 2)
    return round(area, 2)
```

The `calculate_circle_area` function takes the radius as input, asserts that it is non-negative, and then returns the area of the circle rounded to two decimal places.

## User Input and Error Handling

The program prompts the user to enter the desired radius of the circle using the `input()` function and converts the user input to a floating-point number using `float()`.

```python
radius = float(input("Enter the desired radius: "))
```

It then utilizes a try-except block to handle exceptions raised by the `calculate_circle_area` function if the user provides a negative radius. In case of a negative radius, the program will print an error message.

```python
try:
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area}")
except AssertionError as e:
    print(e)
```

This program calculates the area of a circle accurately, while also ensuring that the radius is non-negative and providing appropriate error messages when necessary.
