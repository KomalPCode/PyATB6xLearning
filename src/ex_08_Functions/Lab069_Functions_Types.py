#User defined
# 1. They can't return--> non return
# 2. They return somthing
# 3. They have parameters
# 4. They don't have parameters/arguments

import math

# built in function
result = max(3,4)
print(result)

# User defined function
# 1. No return type and No parameter / Argument
def greet():
    print("Hello")

greet()

# 2. No return type but with argument
def greet_by_name(name):
    print("Hello", name)

greet_by_name("Komal")

# 3. No return type and with default argument
def say_hello_default_argument(name = "Komal"):
    print("Hello", name)

say_hello_default_argument("Pawar")
say_hello_default_argument()

def multiple_args(name1 = "A", name2 = "B"):
    print("mul-->", name1, name2)

multiple_args()
multiple_args("Komal", "Pawar")
multiple_args(name1 = "Komal")
multiple_args(name1 = "Komal", name2 = "Pawar")
multiple_args(name2 = "Pawar")

# 4. Argument + Return Type
def sum_of_two(a, b):
    return a + b

result = sum_of_two(4, 56)
print(result)


def sum_of_two_numbers_with_default(a = 4, b = 56):
    print("I will return the two numbers")
    return a + b

result = sum_of_two_numbers_with_default(a = 100, b = 200)
print(result)
result = sum_of_two_numbers_with_default()
print(result)




