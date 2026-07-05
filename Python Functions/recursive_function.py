# A recursion is when a function calls itself
# A recursive function must have two parts :
    # 1)Base case - a condition that stops function (without base case , function calls itself forever causing stack overflow error)
    # 2)Recursive case - the function calling itself with a modified argument

# EXAMPLE
def factorial(n):
    # Base case
    if n==0 or n==1:
        return 1
    # Recursive case
    else:
        return n*factorial(n-1)
    
print(factorial(5))