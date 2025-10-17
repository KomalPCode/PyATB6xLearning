age = int(input("Enter the age: ").strip())
if age <= 0 or age > 130 :
    print("Enter valid age")
else :
    if age >= 21:
        print("Yes can go to Goa")
    else :
        print("No can't go to Goa")