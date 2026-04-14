thisList = [10,20,30,40,50]


# Incorrect way:
myList = thisList   #thisList is reference to myList

# changes made in myList will automatically also be made in thisList.
myList[0] = 20
print(thisList)
print(myList)

# WAYS TO MAKE COPY OF LIST:

# copy() - makes a copy of List

nums1 = thisList.copy()
print(nums1)

# list() - another way to make copy of list
nums2 = list(thisList)
print(nums2)

# Using slice operator to make copy of list
nums3 = thisList[:]
print(nums3)
