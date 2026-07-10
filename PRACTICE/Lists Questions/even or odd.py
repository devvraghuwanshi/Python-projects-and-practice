thisList = [1,2,3,4,5,6,7,8,9,10]

odd = 0
even = 0

for num in thisList:
    if num%2 == 0:
        even += 1
    else:
        odd += 1

print(f"even numbers:{even}\n odd numbers:{odd}")
