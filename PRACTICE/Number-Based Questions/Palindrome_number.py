# Palindrome number : Same when reversed

num = int(input("Enter Number: "))
onum = num
rev = 0

while num != 0:
    last_digit = num % 10 
    rev = rev * 10 + last_digit
    num = num//10 

if onum == rev:
    print("Palindrome Number")
else:
    print("Not a palindrome Number")