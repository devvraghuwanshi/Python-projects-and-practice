#  Using loop reverse digits

num = int(input("Enter Number: "))
onum = num
rev = 0

while num != 0:
    last_digit = num % 10 
    rev = rev * 10 + last_digit
    num = num//10 

print(f"The reverse of Number {onum} is reverse: {rev}")




