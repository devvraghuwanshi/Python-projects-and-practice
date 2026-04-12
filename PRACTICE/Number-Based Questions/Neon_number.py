# Neon number = A Neon Number is a number where the sum of the digits of its square is equal to the number itself.


num = int(input("Enter Number:"))
onum = num
square = num ** 2

sum = 0

while square != 0:
    ld = square%10
    sum = sum + ld
    square = square//10

if sum==onum : print("Neon Number")
else: print("NOT a Neon Number")

