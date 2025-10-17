
#Problem find the max between 3 numbers

num1 = int(input("Enter a num1: \n"))
num2 = int(input("Enter a num2: \n"))
num3 = int(input("Enter a num3: \n"))

if num1 >= num2 and num1 >= num3:
    print("Max is : ", num1)
elif num2 >= num1 and num2 >= num3:
    print("Max is : ", num2)
else:
    print("Max is : ", num3)

"""
Just for checking

num1 = int(input("Enter a num1: \n"))
num2 = int(input("Enter a num2: \n"))
if num1 > num2:
    print("Max is num1 : ", num1)
else:
    print("Max is num2: ", num2)


#Solution not working

num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))
num3 = int(input("Enter a num3: "))

if num1 >= num2:
    if num1 >= num3:
        print("Max is num1 : ", num1)
elif num2 >= num3:
        print("Max is num2 : ", num2)
    #else:
     #   print("Max is num3 : ", num3)
else:
    print("Max is num3 : ", num3)

#ChatGpt solution using nested if else
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        print("The largest number is:", a)
    else:
        print("The largest number is:", c)
else:
    if b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)

"""