user = int(input("Enter a number:"))
temp = user
count = 0
rev_no = 0
sum_val = 0
while user>0:
    digit = user%10
    # Print the sum of given number
    sum_val += digit
    # Print the reverse of number
    rev_no = rev_no*10+digit
    user = user//10
    # Print the length of the number
    count+=1
# Print the given is a number palindrome or not 
temp = rev_no
if temp == user:
    print(f"{user} is a number palindrome")
else:
    print(f"{user} not a palindrome")
print(f"The length of the number:{count}")
print(f"The sum of a given number is:{sum_val}")
print(f"The reverse of given number is:{rev_no}")


# Swapping of two numbers
num1 = 10
num2 = 20
temp = 0
temp = num1
num1 = num2
num2 = temp
print(f"num1={num1}")
print(f"num2={num2}")

# Without using a third variable temp
num1 = 10
num2 = 20
num1,num2 = num2,num1
print(f"num1={num1}")
print(f"num2={num2}")
        #or
num1 = 10
num2 = 20
num1 = num1+num2 # 10+20 = 30
num2 = num1-num2 # 30-20 = 10
num1 = num1-num2 # 30-10 = 20
print(f"Now, The num1 = {num1}")
print(f"The num2 = {num2}")
        #or
num1 = 10
num2 = 20
num1 = num1 ^ num2 # if we perform XOR operation with same number we get for example in simple terms XOR operation - give 1 when the two operators are different, give 0 when two operators are same 
num2 = num1 ^ num2 # (10 ^ 20) ^ 20 => 10                                              # as same 5 ^ 5 => 0, as same as 5 ^ 0 => 5
num1 = num1 ^ num2 # (10 ^ 20) ^ 10 => 20
print(f"The num1 = {num1}")
print(f"The num2 = {num2}")

    
    
