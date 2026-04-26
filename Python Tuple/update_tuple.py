# Tuple are unchangeable , immutable 
# TO UPDATE TUPLE:
# 1. convert tuple into list
# 2. change the list
# 3. convert list back into tuple

# ADD ITEMS :-

# EXAMPLE-1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
x = tuple(y)
print(x)

# EXAMPLE-2
a = ("apple", "banana", "cherry")
b = list(a)
b.append("mango")
a = tuple(b)
print(a)

# EXAMPLE-3 : Add tuple to tuple
o = ("apple", "banana", "cherry")
p = ("mango",)
o += p
print(o)

# REMOVE ITEMS :-

# EXAMPLE-1
thistuple = ("apple", "banana", "cherry")
c = list(thistuple)
c.remove("apple")
thistuple = tuple(c)
print(thistuple)

# EXAMPLE-2 : del keyword delete tuple completely
thistuple1 = ("apple", "banana", "cherry")
del thistuple1
print(thistuple1) #thistuple1 no longer exists


