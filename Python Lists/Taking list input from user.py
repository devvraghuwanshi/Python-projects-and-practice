# Taking input of list elements from user:

nums = []

n = int(input("Enter number of elements to put in list: "))

for i in range(n):
    num = int(input("Enter number to add in list: "))
    nums.append(num)

print(nums)