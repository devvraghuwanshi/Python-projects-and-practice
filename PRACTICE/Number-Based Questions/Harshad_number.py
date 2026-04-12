# A Harshad Number is a number that is divisible by the sum of its digits.

num = int(input("Enter Number: "))
onum = num

sum = 0

while num!= 0:
    ld = num%10
    sum += ld
    num = num//10

if onum%sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")