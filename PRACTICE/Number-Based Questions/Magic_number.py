# Magic Number = Repeated digit sum equals 1

num = int(input("Enter Number: "))

while num>9:
     sum = 0
     temp = num

     while temp != 0:
          ld = temp%10
          sum += ld
          temp //=10
     
     num = sum

if num == 1: print("Magic Number")
else: print("Not a Magic Number")
