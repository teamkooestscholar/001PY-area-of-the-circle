# Write a function that calculates the area of a circle by a given radius.
#Canane, Jewel Mae P.

import math as m
import time as t

def c_area(radius, d_place=2):
    assert radius >= 0, "Radius cannot be negative!"
    
    area = m.pi * radius ** 2
    return round(area, d_place)

radius = float(input("Enter radius: "))
d_place = int(input("Enter the number of decimal places for rounding: "))

try:
    area = c_area(radius, d_place)
    t.sleep(0.4)
    print("Calculating...")
    t.sleep(0.5)
    print("=" * 50)
    print(f"The area of a circle with radius {radius} is {area:.{d_place}f}")
except AssertionError as e:
    print(e)
