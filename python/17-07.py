# 1. Write a python program to check whether a number entered by the user is positive , negative and zero 
user = int(input("Enter a number:"))
if user>0:
    print(f"{user} is positive")
elif user < 0:
    print(f"{user} is negative")
elif user == 0:
    print(f"{user} is equal to zero")
else:
    print("You entered ivalid input type")

# 2. Write a program to input a number and check whether it is even or odd using an if-else statement
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is a Even")
else:
    print(f"{num} is a Odd")

# 3. Write a python to check whether a given year is a leap year or not
year = int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

# 4. Write a program that takes two numbers from the user and prints which one is greater
num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number2:"))
if num1>=num2:
    print(num1)
else:
    print(num2)

# 5. Ask the user for their age. if the age is 18 or more, print "Eligible to vote", else print "Not eligible"
age = int(input("Enter Your Age:"))
if age>=18:
    print("You are Eligible to Vote")
else:
    print("Not Eligible")

# 6. Grade Checker: Accept marks from the user and print the grade:
#    Marks => 90 -> Grade A
#    75 - 89 -> Grade B
#    60 - 74 -> Grade C
#    40 - 59 -> Grade D
#    Below 40 -> Fail
  

# 7. Number Type Checker: Ask the user to enter a number. Check:
#                        -if it is positive, check if it's even or odd
#                        -if it is negative, print "Negative number"
#                        -if it's zero, print zero
number = int(input("Enter a number:"))
if number<0:
    if number%2==0:
        print(f"{number} is a even number")
    else:
        print(f"{number} is a odd number")
    print(f"{number} is a positive number")
elif number>0:
    print(f"{number} is a negative number")
elif number==0:
    print(f"{number} is equal to zero")
else:
    print("invalid input")

#8.	Simple Calculator: Ask the user to input two numbers and an operator (+, -, *, /). Use if-else to perform the correct operation and show the result.
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
user = input("Enter what are the calculations that you are performed 1=Addition, 2=Subtraction, 3=Multiplication, 4=division")
if user==1 or '+':
    print(num1+num2)
elif user==2 or '-':
    print(num1-num2)
elif user==3 or '*':
    print(num1*num2)
elif user==4 or '/':
    print(num1/num2)
else:
    print("Please enter a valid operation..!")
