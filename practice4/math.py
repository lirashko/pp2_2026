import math

degree = float(input("Input degree: "))
radian = degree * math.pi / 180
print("Output radian:", radian)

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
trapezoid_area = (base1 + base2) * height / 2
print("Expected Output:", trapezoid_area)

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
polygon_area = sides * length ** 2 / (4 * math.tan(math.pi / sides))
print("The area of the polygon is:", polygon_area)

base = float(input("Length of base: "))
parallelogram_height = float(input("Height of parallelogram: "))
parallelogram_area = base * parallelogram_height
print("Expected Output:", parallelogram_area)