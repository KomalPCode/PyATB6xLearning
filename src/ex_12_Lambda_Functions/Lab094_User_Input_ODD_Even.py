# Write a program to calculate Even and Odd
# def find_even_odd(num):
#    if num % 2 == 0:
#       print("Even")
#    else:
#        print("ODD")

user_input = int(input("Enter a number: "))

check_even_odd_fun = lambda num: "Even" if num % 2 == 0 else "Odd"
result_l = check_even_odd_fun(user_input)
print(result_l)