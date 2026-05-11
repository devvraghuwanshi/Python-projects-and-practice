# Python Set Methods - Complete Guide

# Creating sets
s = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 2, 3}

# add() - Adds a single element to the set
s.add(10)
print(s)  # {1, 2, 3, 4, 5, 10}

# remove() - Removes an element; raises error if not found
s.remove(10)
print(s)  # {1, 2, 3, 4, 5}

# discard() - Removes an element; no error if not found
s.discard(100)  # No error even though 100 doesn't exist
print(s)

# pop() - Removes and returns an arbitrary element
removed = s.pop()
print(f"Removed: {removed}")

# clear() - Removes all elements from the set
temp = {1, 2, 3}
temp.clear()
print(temp)  # set()

# copy() - Creates a shallow copy of the set
s_copy = s.copy()
print(s_copy)

# union() - Returns a new set with elements from both sets
result = s.union(s2)
print(result)  # All elements from s and s2

# update() - Adds all elements from another set to the current set
s.update(s2)
print(s)

# intersection() - Returns a new set with elements common to both sets
result = s.intersection(s2)
print(result)  # Elements present in both s and s2

# intersection_update() - Keeps only elements found in both sets
s.intersection_update(s2)
print(s)

# difference() - Returns a new set with elements in first set but not in second
result = s.difference(s2)
print(result)

# difference_update() - Removes elements found in another set
s.difference_update(s2)
print(s)

# symmetric_difference() - Returns elements in either set but not in both
result = s.symmetric_difference(s2)
print(result)

# symmetric_difference_update() - Updates set with symmetric difference
s.symmetric_difference_update(s2)
print(s)

# issubset() - Checks if all elements of set are in another set
is_sub = s3.issubset(s)
print(is_sub)  # True if s3 is subset of s

# issuperset() - Checks if set contains all elements of another set
is_super = s.issuperset(s3)
print(is_super)

# isdisjoint() - Checks if two sets have no elements in common
is_disjoint = s.isdisjoint(s2)
print(is_disjoint)  # True if no common elements

# len() - Returns number of elements in the set
count = len(s)
print(count)