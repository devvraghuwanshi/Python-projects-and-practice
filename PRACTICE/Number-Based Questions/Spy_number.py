# Spy number = Sum and product of digits are equal.

num = int(input("Enter Number: "))

sum = 0
product = 1

while num != 0:
    ld = num%10
    sum += ld
    product *= ld
    num = num//10

if sum == product : print("Spy Number")
else : print("NOT a Spy Number")