# Create tuple -> assign values to it -> PACKING
# extract values back into variable -> UNPACKING

# EXAMPLE-1 :-

fruits1 = ("apple", "banana", "cherry")

(green,yellow,red) = fruits1

print(green)
print(yellow)
print(red)

# number of variable should be equal to number of values in tuple if not use *(asterisk) to collect remaining values

# EXAMPLE-2 :- using *(asterisk)
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green,yellow,*red) = fruits2
(green,*yellow,red) = fruits2

print(green)
print(yellow)
print(red)