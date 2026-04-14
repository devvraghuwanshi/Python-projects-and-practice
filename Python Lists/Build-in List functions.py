thisList = [10,30,40,50,70,100,True,0]

# len(listName) - Returns number of elements
print(len(thisList))

# max(listName) - returns largest Number
print(max(thisList))

# min(listName) - returns smallest Number
print(min(thisList))

# sum(listName) - returns sum of all elements
print(sum(thisList))

# sorted(listName) - returns new sorted list
print(sorted(thisList))

# any(listName) - returns True if any element is true 
print(any(thisList))

# all(listName) - returns True if all elements are true
print(all(thisList))

# enumerate(listName) - gives index + value
for i,val in enumerate(thisList):
   print(i,val)

# zip(list1,list2) - combines multiple lists
thisList2 = [200,300,400]
print(list(zip(thisList,thisList2)))

# map(function,listName) - applies function to each elements
numberss = [1,2,3,4,5]
print(list(map(lambda x: x**2,numberss)))

# filter(condition,listName) - filters element based on conditions
print(list(filter(lambda x: x%2==0,numberss)))