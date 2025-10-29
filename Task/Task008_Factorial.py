num = int(input("Enter a program which fact you want to get : "))

fact = 1

if num < 0:
    print("Factorial is not defined")

if num == 0:
    print("Factorial is : ",fact)
else:
    for i in range(1,num+1):
        fact = fact * i

print(fact)