# You cannot directly copy like dict1 = dict2 , here dict2 will only be reference to dict1 and any changes made to dict1 will also be made in dict2.

# CORRECT way to copy dictionary -
dict1 = {
    "Dev" : "Raghuwanshi",
    "Sagar" : "Kashyap"
}
# Method 1 -
dict2 = dict1.copy()
print(dict2)

# Method 2 - 
dict3 = dict(dict1)
print(dict3)