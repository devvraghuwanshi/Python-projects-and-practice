# frozenset : Immutable version of set

# Creating frozen set :
fruits = frozenset(["apple" , "banana" , "mango"])
print(fruits)
print(type(fruits))

fruits2 = frozenset(["cherry","mango","apple"])
# some methods :
    
fruits_copy = fruits.copy()       # Returns a shallow copy of the frozenset
print(fruits.difference(fruits2)) # Returns elements in fruits but not in fruits2
  
print(fruits.intersection(fruits2))    # Returns common elements between fruits and fruits2
print(fruits.isdisjoint(fruits2))     # Returns True if fruits and fruits2 have no common elements
print(fruits.issubset(fruits2))      # Returns True if fruits is a subset of fruits2
print(fruits.issuperset(fruits2))   # Returns True if fruits is a superset of fruits2
print(fruits.symmetric_difference(fruits2))   # Returns elements in either fruits or fruits2 but not both
print(fruits.union(fruits2))     # Returns all unique elements from both frozensets