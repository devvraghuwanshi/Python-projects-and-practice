thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Positive index - 0,1,2,3,4,....
print(thistuple[2])

# negative index - .......,-3,-2,-1
print(thistuple[-1])

# slicing:

print(thistuple[2:3])
print(thistuple[:3])
print(thistuple[0:])
print(thistuple[-4:-1])

# membership operation : checks of item exist in tuple

if "apple" in thistuple:
    print("apple exist")