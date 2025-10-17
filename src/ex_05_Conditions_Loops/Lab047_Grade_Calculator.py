# Grade Calculator
# Write a program that calculates and displays the letter Grade
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter score: ").strip())

if score > 100 or score <= -1:
    print("Score is invalid. you can't get a grade")
else:
    if score >=90 and score <=100:
        print("Your grade is A")
    elif score >= 80 and score <=89:
        print("Your grade is B")
    elif score >= 70 and score <=79:
        print("Your grade is C")
    elif score >= 60 and score <=69:
        print("Your grade is D")
    else:
        print("Your grade is F")


#Handling of float and string output is pending---try catch
