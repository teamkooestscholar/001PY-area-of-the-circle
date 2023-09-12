import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = math.pi * (radius ** 2)
        return area

# Function to calculate the circumference of a circle
def calculate_circle_circumference(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        circumference = 2 * math.pi * radius
        return circumference

# Function to calculate the diameter of a circle
def calculate_circle_diameter(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        diameter = 2 * radius
        return diameter

# Menu-driven program
while True:
    print("\nChoose an operation:")
    print("1. Calculate the area of a circle")
    print("2. Calculate the circumference of a circle")
    print("3. Calculate the diameter of a circle")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        circle_area = calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is {circle_area:.2f}")
    elif choice == '2':
        radius = float(input("Enter the radius of the circle: "))
        circle_circumference = calculate_circle_circumference(radius)
        print(f"The circumference of the circle with radius {radius} is {circle_circumference:.2f}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        circle_diameter = calculate_circle_diameter(radius)
        print(f"The diameter of the circle with radius {radius} is {circle_diameter:.2f}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
