thisList = [10,20,30,40,50]

first_max = second_max = float('-inf')

for num in thisList:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num>second_max and num != first_max:
        second_max = num
print(f"Second Largest is {second_max}")


