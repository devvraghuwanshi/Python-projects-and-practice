# Boolean represents one of two values : True or False

# bool(value) - this function allows you to evaluate any value and return true or false

# Boolean Practice - Truthy and Falsy Values

# Falsy values
print("Falsy Values:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))


# Truthy values
print("Truthy Values:")
print(bool(True))
print(bool(10))
print(bool(-5))
print(bool(3.14))
print(bool("Python"))
print(bool(" "))      # String with a space
print(bool([1, 2, 3]))
print(bool((1, 2)))
print(bool({"name": "Dev"}))
print(bool({1, 2, 3}))