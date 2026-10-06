# *args (arbitary arguments) -
# allows function to take any number of positional parameters , by adding * befor parameter name.
# this way funcitons recieves tuple of arguments

def fun1(*kids):
    print(type(kids))
    print(f"The yougest child is : {kids[0]}")
    print(f"the oldest child is : {kids[1]}")

fun1("Dev","Diksha")

# Using *args with regular arguments -
def fun11(name,*lnames):
    print(f"Hello, {name}")
    print(f"first last name option: {lnames[0]}")
    print(f"Second last name option: {lnames[1]}")

fun11("Dev","Raghuwanshi","patel")


# **kwargs(arbitary keyword arguments) -
# allows funtions to take any number of keyword parameters , by adding ** before parameter name.
# this way function recieves dictionary of arguments

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")  