def find_square(number):
    if number > 0:
        square = number * number
    return square


square_of_number = find_square(int(input("Enter a number: ")))
print(square_of_number)
