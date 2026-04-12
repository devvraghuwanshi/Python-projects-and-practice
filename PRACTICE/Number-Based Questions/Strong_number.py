# Strong Number = Sum of factorial of digits

num = int(input("Enter Number: "))
onum = num
sum = 0

while num!= 0:
    last_digit = num%10
    fact = 1 
    for i in range(last_digit,0,-1):
        fact *= i
    sum += fact
    num = num//10

if onum == sum:
    print("Strong Number")
else:
    print("NOT a Strong Number")