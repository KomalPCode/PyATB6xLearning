def area_Triangle(side1, side2, side3):
    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 == side2 == side3:
            return "It's a Equilateral triangle"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "It's a Isosceles triangle"
        elif side1 != side2 != side3:
            return "It's a Scalene triangle"


type_of_string = area_Triangle(int(input("Enter side1 : ")), int(input("Enter side2 : ")), int(input("Enter side3 : ")))
print(type_of_string)

