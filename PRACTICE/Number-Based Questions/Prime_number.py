# Prime Number: Only divisible by 1 and itself

num = int(input("Enter Number: "))
onum = num
flag = 0

if num <= 1:
    print(f"{num} is NOT a prime number")
else:
    for i in range(2,num):
         if num % i == 0:
           flag += 1
           break
 
    if flag == 0:
       print(f"{onum} is a Prime Number")
    else:
       print(f"{onum} is NOT a Prime Number")
