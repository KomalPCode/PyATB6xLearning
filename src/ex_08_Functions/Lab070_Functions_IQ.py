# Create a program to find sum of three numbers from the user input
# if user doesn't enter any number, use default as 100, 200, 300

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

def sum_of_three_numbers(n1 = 100, n2 = 200, n3 = 300):
    return n1 + n2 + n3

result = sum_of_three_numbers(num1, num2, num3)
print(result)
result1 = sum_of_three_numbers()
print(result1)
result2 = sum_of_three_numbers(n1 = 10)
print(result2)
result3 = sum_of_three_numbers(n1 = 10, n2 = 20)
print(result3)
result4 = sum_of_three_numbers(n1 = 10, n2 = 20, n3 =  40)
print(result4)
