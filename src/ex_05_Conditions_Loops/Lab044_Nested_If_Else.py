#Find the positive number is Even or Odd

num = int(input("Enter the number: "))

if num >= 0 :
    if num % 2 == 0 :
        print("Number is even")
    else :
        print("Number is odd")
else :
    print("Number is negative")

#Short one liner condition using ternary operator
if num >= 0 :
        print("Number is even" if num % 2 == 0 else "Number is odd")
else :
    print("Number is negative")