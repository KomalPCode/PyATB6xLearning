# Write a program to take a user age and let him know if he can go to the club

#Step 1 Decide input and output
#i/p - age, int
#o/p - String (Result -> can go to club or not)

#Step 2 Rough Logic(Brute force)
"""
age > 21 -> print can go
age < 21 -> print can't go
"""
#Step 3 write the logic
age = int(input("Enter the age: "))
if age >= 21:
    print("Yes can go to Goa")
else :
    print("No can't go to Goa")

#Step 4 :Check for the edge cases
#We should consider edge cases such as
#Negative edges or extremely high values-> Program will break
#Non numeric input->ABC
#Age is invalid .>130

#Step 5 Optimize the code
#Handle all the edege cases


