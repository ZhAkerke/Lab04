# Exercise 1
import math
n = int(input("Input degree: "))
print("Output radian: ", "{:.6f}".format(math.radians(n)))

# Exercise 2
h = int(input("Height: "))
x = int(input("Base, first value: "))
y = int(input("Base, second value: "))
S = ((x+y)/2)*h
print("Expected Output:")

# Exercise 3
import math
def area_p(n, s):
    area = (1/4) * n * s**2 * (1/math.tan(math.pi/n))
    return area

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = area_p(n, s)
print("The area of the polygon is: ", area)

# Exercise 4
def prll_area(b, h):
    area = b * h
    return area

b = float(input("Length of base: "))
h = float(input("Heigth of parallelogram: "))
area = prll_area(b, h)
print("Expected Output: ", area)