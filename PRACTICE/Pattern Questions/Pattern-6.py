# Ques-6 : Diamond shape
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


rows = 4

# upper pyramid
for i in range(1,rows+1):
    # space
    for j in range(rows-i):
        print(" ",end="")
    # stars
    for k in range(2*i - 1):
        print("*",end="")
    print()

# lower Pyramid
for i in range(rows-1,0,-1):
    # space
    for j in range(rows-i):
        print(" ",end="")
    # stars
    for k in range(2*i-1):
        print("*",end="")
    print()