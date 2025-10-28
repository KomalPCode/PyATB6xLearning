"""
Given a Number a number you need to calculate the factorial of that number

n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1



num = int(input("Enter a number to find a factorial: "))

for i in range(num,0, -1 ):
    num = num * (num-1)
    print(num)
"""
num = int(input("Enter a number to find a factorial: "))

fact = num
i = num
while(i > 1):
    fact = fact * (i-1)
    i = i - 1
print(fact)

