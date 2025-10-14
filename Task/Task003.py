import math
radius = float(input("Enter the radius of circle : "))
print(radius)
#area = 3.14 * radius * radius
#area = 3.14 * (radius**2)
#area = 3.14 * pow(radius, 2)
area = math.pi * radius ** 2
#This is called string data formatting, Python f-string, formatted string literals
print(f"The area of the circle is {area:.2f}")