#Submission Change
#import math #If math.pi is implemented the value will not result with decimal places.
try:
    radius = float(input("Register The Radius Length: "))
    
    # [V] This implies that the radius should not be less than 0 or a negative number, but can be 0.
    assert radius >= 0, "Radius must be non-negative and should not be less than 0"

    Deci = int(input("Enter the number of decimal places for rounding: " ))
    Pie = 3.141592653589793238462643

    # [V] Formula to compute the Radius of the Circle
    #math.pi could be utilized for this process however it does not result with decimal points.
    #CircArea = round(Pie*radius*radius, Deci) #functions the same, just different layout.
    CircArea = round(Pie*radius**2) #
    
    
    # [V] Output
    print("Result of Evaluated Radius of The Circle: ", CircArea) 

# [V] Error Prompt If Value is Null or Invalid
except ValueError: 
    print("Seems Like You've registered an Invalid Variable. Try Again.")
