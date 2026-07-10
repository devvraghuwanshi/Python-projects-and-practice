nums = [10,20,30,10,50,30,70,20]

unique = []

for num in nums:
   frequency = nums.count(num)

   if frequency == 1:
      unique.append(num)

print(unique)