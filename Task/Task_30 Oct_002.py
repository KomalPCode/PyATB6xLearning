""""
Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 =side3 → isoceles
o/p = result in string - iso, eq, scalene

"""
#My Solution
def area_Triangle(side1, side2, side3):
    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 == side2 == side3:
            return "It's a Equilateral triangle"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "It's a Isosceles triangle"
        else:
            return "It's a Scalene triangle"


type_of_string = area_Triangle(int(input("Enter side1 : ")), int(input("Enter side2 : ")), int(input("Enter side3 : ")))
print(type_of_string)

"""
# Ideal output
side1 = float(input("Enter side1 : "))
side2 = float(input("Enter side2 : "))
side3 = float(input("Enter side3 : "))

def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "It's a Equilateral triangle"
            elif a == b or b == c or a == c:
                return "It's a Isoceles triangle"
            else:
                return "It's a Scalene triangle"
        else:
            return "Not a triangle"
    else:
        return "Not a valid length"


result = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as :{result}")
"""