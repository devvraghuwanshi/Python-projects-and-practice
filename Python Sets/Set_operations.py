# Sets operations -
set1 = {1,2}
set2 = {2,3}
set3 = {5,3}
mytuple = (6,7,8,9,2,1)


# NOTE - You can only use methods to join set with other data type, but cannot use operators to join eith other datatype.

# 1. union() or | operator - joins all elements from both sets
print(set1.union(set2))
print(set1 | set2)
print(set1.union(set2,set3))
print(set1|set2|set3)
print(set1.union(mytuple))

# 2. intersection() or & operator - will return new set with common elements 
print(set1.intersection(set2))
print(set1&set2)

# intersection_update() - keep common elements and change original set instead of returning new set
# set1.intersection_update(set2)
# print(set1)
print(set1.intersection(mytuple))

# 3. difference()  or -operator - The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
print(set1.difference(set2))
print(set1 - set2)

# difference_update() - change original set instead of returning new set
# set1.difference_update(set2)
# print(set1)

# 4. symmetric_difference() or ^ operator - will keep only the elements that are not present in both sets
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

# symmetric_difference_update() - change original set instead of returning new set
# set2.symmetric_difference_update(set2)
# print(set1)
print(set1.symmetric_difference(mytuple))