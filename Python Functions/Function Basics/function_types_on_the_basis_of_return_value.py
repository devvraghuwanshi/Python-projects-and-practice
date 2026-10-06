# Function type on the basis of return value : 

# 1. function with no argument and no return value -
def fun1():
    print("I am function with no argument and no return value")

fun1()

# 2. function with argument and no return value -
def fun2(name):
    print(f"my name is {name}")

fun2("Dev")

# 3. function with no argument and return value -
def fun3():
    return 100

num = fun3()
print(num)

# 4. function with argument and return value -
def add(a,b):
    return a+b

result = add(10,20)
print(result)