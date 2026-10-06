# Example-2 : Returns a function

# divident / divisor = quotient

# Outer Function
def divisor(x):
    # Inner Function
    def divident(y):
        return y / x
    # Return function
    return divident

# Saving value of divident function in variable
divide = divisor(2)  # x=2

# setting value of y in divident
print(divide(10))    #y=2

