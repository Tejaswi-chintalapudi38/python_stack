#Section A: Easy (3 questions × 2 marks = 6 marks)
#  1.(2 marks) What will be the output and data type of the following code?
a = input("Enter value: ")
print(a * 2)
print(type(a))

# 2.(2 marks) Convert the string '123.45' into a float, and print its integer part only.
string = '123.45'
floating = float(string)
print(round(floating))

# 3.(2 marks) Identify the correct output of this expression:
result = 10>5 and 3<1
print(result)

# Section B: Medium (11 questions × 4 marks = 44 marks)
#  4.(4 marks) Write a program to take a number from the user and check whether it is:
#              o	Divisible by 3 and 4 → print “Divisible by both”
#              o	Only divisible by 3 → print “Divisible by 3”
#              o	Only divisible by 4 → print “Divisible by 4”
#              o	Otherwise → print “Not divisible
number = int(input("Enter a number:"))
if number%3 == 0 and number%4==0:
    print("Divisible by both")
else:
    if number%3==0:
        print("divible by 3")
    else:
        if number%4==0:
            print("divisible by 4")
        else:
            print("Not divisible")
        
# 5.(4 marks) Accept two numbers from the user and print whether their sum is even or odd, and whether it is greater than 50 or not.
num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
summ = num1+num2
if summ%2==0:
    print("Even")
else:
    print("odd")
if summ>50:
    print("and sum is greater than 50")

# 6.(4 marks) Rewrite the following using elif and correct syntax errors:
numeral = int(input("Enter a number:"))
if numeral>0:
    print("Negative")
elif numeral==0:
    print("Equal to zero")
else:
    print("Positive")

# 7.(4 marks) Write a program that asks for a password (input from user).
#             If the password is incorrect, print “Try again”, and ask again. Repeat until correct password ("admin123") is entered.
#               1.Hint: You have to use an infinite while loop and break statement.
while True:
    password = input("Enter password:")
    if password=="admin123":
        break
    else:
        print("Try again")
    
# 8.(4 marks) Print all odd numbers between 1 to 20 using a loop, but skip 13 and 17 using the continue statement.
for i in range(1,20):
    if i%2!=0:
        if i==13 or i==17:
            continue
        print(i)
    
# 9.(4 marks) Write a program to find the sum of first n natural numbers. Solve the question in as many ways as you can.
summ = 0
n = int(input())
for i in range(1,n+1):
    summ+=i
print(sum)

# 10.(4 marks) Ask the user to enter a number.Print “Buzz” if the number is divisible by 7 or ends with even digit. Otherwise, print “Not a Buzz number”.
user_input = int(input("Enter a number:"))
if user_input%7==0 or (user_input%10)%2==0:
    print("Buzz")
else:
    print("Not buzz")

# 11.(4 marks) What will be the output of this code?Explain each step:
x = 5
while x > 0:
    if x == 3:
        x -= 1
        continue
    print(x)
    x -= 1

# 12.(4 marks) Write a program that:
#   •	Takes an integer input
#   •	If it’s a multiple of 4, prints square of the number
#   •	If it’s a multiple of 5, prints cube of the number
#   •	Otherwise, prints the number itself
integer_input= int(input())
if integer_input%4==0:
    print(integer_input**2)
elif integer_input%5==0:
    print(integer_input**3)
else:
    print(integer_input)

# 13.(4 marks) Write a program to count how many alphabets are there in a string input from the user.
#              Example input: abc123 → Output: 3
user_string = input().lower()
count = 0
alphabets = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for u  in user_string:
    if u in alphabets:
        count+=1
print(count)

# 14.(4 marks) What is the role of the pass statement in Python? Use an example of an empty for loop using pass.
#  Pass statement is a one of the jumping statement it acts like passing a statement without giving any result
#  it results nothing or empty we use these pass statement in the case of we don't have any condition or result to print
for i in range(1,10):
    pass

