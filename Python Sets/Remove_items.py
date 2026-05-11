# Methods to remove an items in set :-
fruits = {"apple","mango","banana","grapes","watermelon","blueberry"}

# 1. remove(value) - used to remove an item from set , if the item to remove does not exist remove() will raise an error
fruits.remove("apple")
# fruits.remove("cherry")
print(fruits)

# 2. discard(value) - used to remove an item from set , if the item to remove does not exist discard() will NOT raise an error
fruits.discard("mango")
fruits.discard("cherry")
print(fruits)

# 3. pop() - used to remove random item
x = fruits.pop()     #return value of pop() is removed item
print(f"Set is : {fruits} and remove item is {x}")

# 4. clear() - empties the set
fruits.clear()
print(fruits)

# 5. del setName - del keyword will delete set completely
extra_fruits = {"banana","grapes","watermelon"}
del extra_fruits
print(extra_fruits)