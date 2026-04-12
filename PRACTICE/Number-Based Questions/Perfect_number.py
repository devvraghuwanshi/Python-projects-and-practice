# Perfect Number : Sum of proper divisors = number
# Proper divisors = all numbers that divide the number except itself

num = int(input("Enter Number: "))
onum = num

sum = 0

for i in range(1,num):
    if num % i == 0:
        sum += i
if onum == sum:
    print(f"{onum} is Perfect Number")
else:
    print(f"{onum} is NOT a Perfect Number")


