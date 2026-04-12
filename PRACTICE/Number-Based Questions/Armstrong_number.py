# Armstrong Number : Sum of (each digit ^ n) = original number

num = int(input("Enter Number: "))
onum = num

arm = 0
digits = len(str(num))

while num != 0:
    last_digit = num % 10
    arm = arm + (last_digit**digits)
    num = num//10

if onum == arm:
    print(f"{onum} is a Armstrong Number")
else:
    print(f"{onum} is Not a Armstrong Number")
