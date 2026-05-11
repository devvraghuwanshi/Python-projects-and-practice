# Once a set is created, you cannot change its items, but you can add new items.
fruits = {"apple","mango","banana"}

# Methods to add items in list ->

# 1. add(value) - used to add one item
fruits.add("cherry")
print(fruits)

# 2. update(iterable_name) - add any iterable object
other_fruits = ["grapes","watermelon","blueberry"]
fruits.update(other_fruits)
print(fruits)