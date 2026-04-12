# An Automorphic Number is a number whose square ends with the same number itself.

num = int(input("Enter Number: "))
square = num ** 2

digits = len(str(num))   # count digits

if square % (10 ** digits) == num:
    print("Automorphic Number")
else:
    print("NOT an Automorphic Number")
