nums = [-3,-2,-1,1,2,3]

positive_numbers = []
negative_numbers = []
for num in nums:
    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)

print(positive_numbers)
print(negative_numbers)