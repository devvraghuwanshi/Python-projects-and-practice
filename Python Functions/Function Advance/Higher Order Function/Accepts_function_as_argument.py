# Higher Order Function: A function that either -
#                        1.) Accepts a function as an argument.
#                        2.) Returns a function.

# Example-1 : Accepts function as an argument

# Function-1
def loud(text):
    return text.upper()

# Function-2
def quite(text):
    return text.lower()

# Higher order function that accepts functio as argument
def hello(func):
    text = func("Hello")
    print(text)

# Calling Higer order function
hello(loud)
hello(quite)
