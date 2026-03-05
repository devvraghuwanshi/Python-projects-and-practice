# fromat() = returns the specified value(s) and insert them inside the string placeholder.

str = "this is the {price:.2f} of this product"
print(str.format(price = 50))

# Placeholder syntax = {key:formating type}

# F-string = to specify f-sting simply put a f in front of string literal and add {} as placeholder for variables and other operations.
fname = "Dev"
age = 21
str2 = f"My name is {fname} and i am {age} years old"
print(str2)