# # Write a function that calculates the area of a circle by a given radius.
def calculate_circlearea():
pass
import math

def calculate_circle_area(radius, decimal_places=2):
    try:
        assert radius >= 0, "Radius cannot be negative"
        area = math.pi * radius ** 2
        rounded_area = round(area, decimal_places)
        return rounded_area
    except AssertionError as e:
        return str(e)

if name == "main":
    radius = float(input("Enter the radius of the circle: "))
    decimal_places = int(input("Enter the number of decimal places for rounding: "))

    area = calculate_circle_area(radius, decimal_places)

    if isinstance(area, float):
        print(f"The area of the circle with radius {radius} is: {area}")
    else:
        print(area)
------------------------------
EVEN OR ODD
function checkNumber(input) {
  const result = isNaN(input)
    ? "Error: Not a valid number"
    : input % 2 === 0
    ? input >= 0
      ? "Positive Even"
      : "Negative Even"
    : input >= 0
    ? "Positive Odd"
    : "Negative Odd";

  return result;
}

// Example usage:
console.log(checkNumber(4));       // Positive Even
console.log(checkNumber(7));       // Positive Odd
console.log(checkNumber(-2));      // Negative Even
console.log(checkNumber(-9));      // Negative Odd
console.log(checkNumber("My Name is Jay Em")); // Error: Not a valid number
----------------------------------
CELSIUS TO FARENHEIGHT
function checkNumber(input) {
  const result = isNaN(input)
    ? "Error: Not a valid number"
    : input % 2 === 0
    ? input >= 0
      ? "Positive Even"
      : "Negative Even"
    : input >= 0
    ? "Positive Odd"
    : "Negative Odd";

  return result;
}

// Example usage:
console.log(checkNumber(4));       // Positive Even
console.log(checkNumber(7));       // Positive Odd
console.log(checkNumber(-2));      // Negative Even
console.log(checkNumber(-9));      // Negative Odd
console.log(checkNumber("My Name is Jay Em")); // Error: Not a valid number
--------------------------------------------------------
------------------------------------------------------------
REVERSE A STRING
function checkNumber(input) {
  const result = isNaN(input)
    ? "Error: Not a valid number"
    : input % 2 === 0
    ? input >= 0
      ? "Positive Even"
      : "Negative Even"
    : input >= 0
    ? "Positive Odd"
    : "Negative Odd";

  return result;
}

// Example usage:
console.log(checkNumber(4));       // Positive Even
console.log(checkNumber(7));       // Positive Odd
console.log(checkNumber(-2));      // Negative Even
console.log(checkNumber(-9));      // Negative Odd
console.log(checkNumber("My Name is Jay Em")); // Error: Not a valid number
----------------------------------------------------
FIND THE MAXIMUM NUMBER
# # Write a function that returns the largest element in a list.
def findmaximum():
pass
def find_max_and_min(numbers):
    if not numbers:
        return "Your list is empty, cannot find maximum or minimum."

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum

Example usage:
numbers_list = [5, 2, 9, 1, 7, 4, 8]
result = find_max_and_min(numbers_list)
print("Maximum:", result[0])
print("Minimum:", result[1])
-------------------------------------------------
