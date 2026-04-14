list_1 = [10,20,30,40,50]
list_2 = [60,70,80,90,100]

# Using + operator
print("Using + operator\n")
list_3 = list_1 + list_2
print(list_3)

# Using loops
print("Using loops\n")

for x in list_2:
    list_1.append(x)
print(list_1)

# Using extend() method
print("Using extend() method\n")
list_1.extend(list_2)
print(list_1)