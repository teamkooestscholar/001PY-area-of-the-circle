import math as M  
Radius = float (input ("Please enter a radius: "))  
area_of_circle = M.pi* Radius * Radius
decimal_places = int(input("Please enter the number of decimal places: "))
rounded_area = round(area_of_circle, decimal_places)
print (f"The area for the circle is: {rounded_area:.{decimal_places}f}")
