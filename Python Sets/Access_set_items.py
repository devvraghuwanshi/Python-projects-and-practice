# Cannot access set items by index

# But can loop through/Iterate set items :-

my_set = {1,2,3,4,5,6}

for x in my_set:
    print(x)

# Using membership operators in set :
# in - checks if element is present in set
if 1 in my_set:
    print("1 is present")

# not in - checks if element is not present in set
if 7 not in my_set:
    print("7 is not present")
