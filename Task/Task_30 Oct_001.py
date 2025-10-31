"""
Q - Create a function which will take a positive number from the user and perform square of the number?

i/o = 3

o/p = 9

"""
def find_square(number):
    if number > 0:
        square = number * number
    return square


square_of_number = find_square(int(input("Enter a number: ")))
print(square_of_number)
