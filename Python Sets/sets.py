# Sets:
# Unordered → no fixed position
# Mutable → can add/remove items
# Unique elements only
# Elements must be hashable (immutable types like int, string, tuple)


# CREATING SETS:-

# 1.Using curly braces -
my_set = {1,2,3,4}
print(my_set)
print(type(my_set))

# 2.Using constructor -
my_set2 = set([1,2,3,4])
print(my_set2)

# 3.Empty set -
wrong_empty_set = {}          #Creates a dictionary not set
correct_empty_set = set()

print(type(wrong_empty_set))
print(type(correct_empty_set))

# Length of set - len(set_name)
print(len(my_set))

# Different datatypes -
diff_sets = {"dev",2,22.5,True,False,None}
print(diff_sets)