# A Kaprekar Number is a number whose square can be split into two parts such that their sum equals the original number.

num = int(input("Enter Number: "))

square = num ** 2

digits = len(str(num))

# Splitting square
right = square%(10**digits)
left = square//(10**digits)
sum = right + left

if sum == num:
    print("Kaprekar Number")
else:
    print("NOT a Kaprekar Number")