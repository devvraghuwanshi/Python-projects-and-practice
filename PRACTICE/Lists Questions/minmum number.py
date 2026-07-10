thisList = [20,50,100,200,60]

# Using Build-in function
print(f"Minimum number is {min(thisList)}")

# Using Loops

min_num = thisList[0]

for num in thisList:
    if num < min_num:
        min_num = num
print(f"Minimum number in this list is {min_num}")