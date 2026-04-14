thisList = ["apple","banana","mango"]

# Using for loop:
for x in thisList:
    print(x)


# Loop through the index Numbers:
for i in range(len(thisList)):
    print(thisList[i])


j = 0
# Using While loop:
while j < len(thisList):
    print(thisList[j])
    j = j + 1


# Using List Comprehension: 
[print(x) for x in thisList]