# Perfect Number - the perfect number is said to be a positive integer the sum of its divisors is equal to itself is called perfect number

# Check if the given number is a perfect number
n = int(input("Enter a number:"))
sum_val = 0
for i in range(1,n):
    if n%i == 0:
        sum_val += i
if sum_val == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

# Print all the perfect numbers in the given range
low = int(input("Enter lowest number: "))
high = int(input("Enter highest number: "))

for num in range(low, high+1):
    sum_div = 0
    for i in range(1, num):  
        if num % i == 0:     
            sum_div += i     
    if sum_div == num:
        print(num, "is a Perfect Number")


# Print the primes in a given number
number = int(input("Enter a number:"))
num_length = len(number)
for i in range(num_length):
    digit = number%10
    if digit in [2, 3, 5, 7]:
        print(digit)
    number = number//10
           #or
number2 = int(input("Enter a number:"))
while number2>0:
    digit = number%10
    if digit in [2, 3, 5, 7]:
        print(digit)
    number = number//10

# Sum of matrix elements
list1 = [[1, 2, 3],[-5, 6, 7],[10, 12, 8]]
sum_val = 0
for i in list1:
    for j in i:
        sum_val+=j
print(sum_val)

# Reverse of a string
str = input("Enter a string:")
print(str[::-1])

str2 = input("Enter another one:")
reverse_str = reversed(str2)
print(reverse_str)

str3 = input("Enter a string:")
rev_str = ""
for i in str3:
    rev_str = i+rev_str
print(rev_str)
