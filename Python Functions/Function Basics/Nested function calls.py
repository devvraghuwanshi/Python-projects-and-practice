# Nested Function calls : Function calls inside other function calls.
#                         Innermost function calls are resolved first.
#                         returned value is used as argument for the next outer function 


# Without nested function calls:
num = input("Enter positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# With Nested function calls:
print(round(abs(float(input("Enter Positive number: ")))))