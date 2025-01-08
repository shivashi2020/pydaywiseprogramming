# 3. Python program to find the area of a triangle whose sides are given

#To find the area of a triangle when only the lengths of its three sides are known, you can use Heron's formula:.

import math

try:
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is: ", area)
except:
    print("Please enter a valid numerical value.")