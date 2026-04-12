# A Happy Number is a number that eventually becomes 1 when you repeatedly replace it with the sum of the squares of its digits.

num = int(input("Enter Number: "))


while num!= 1:
    sum = 0
    temp = num

    while temp != 0:
        ld = temp%10
        sum += (ld**2)
        temp //= 10
    
    num = sum

if num == 1:
    print("Happy Number")
else:
    print("NOT a Happy Number")

