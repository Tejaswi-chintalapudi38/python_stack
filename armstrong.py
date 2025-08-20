num = int(input("Enter a number: "))
n = len(str(num))
temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** n
    temp //= 10

if sum_val == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
