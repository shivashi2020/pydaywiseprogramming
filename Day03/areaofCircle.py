#Python program to find the circumference and area of a circle with a given radius

import math
def areaofCircle():
    try:
        radius =  int(input("Enter radius of the circle \n"))
       # return round(math.pi * radius * radius,2)
        return round(math.pi * math.pow(radius,2),2)
    except ValueError:
        print("Enter valid Number")


print(areaofCircle())
