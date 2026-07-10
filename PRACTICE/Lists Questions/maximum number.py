thisList = [10,20,30,50,40]

# Using Build-in function
print(f"Maximum number is {max(thisList)}")

# Using logic
max_num = thisList[0]

for num in thisList:
    if num > max_num:
        max_num = num

print(f"Maximum number in this list is {max_num}")