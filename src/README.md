# Calculate the Area of a Circle

This Python program calculates the area of a circle based on a user-provided radius.

## Function for Calculation

The code defines a single function for calculating the area of the circle:

```python
def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    """
    return 3.14159 * (radius ** 2)
```

The `calculate_circle_area` function takes the radius as input and returns the area of the circle.

## User Input

The program prompts the user to enter the desired radius of the circle using the `input()` function. It then converts the user input to a floating-point number using `float()`.

```python
radius = float(input("Enter the desired radius: "))
```

## Calculation and Output

After obtaining the radius from the user, the program calculates the area of the circle using the `calculate_circle_area` function and displays the result.

```python
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}")
```
