#1)Is a number positive or negative
n = int(input("Enter a number:"))
if n>0:
    print(f"{n} is a negative number")
elif n<0:
    print(f"{n} is a positive number")
elif n==0:
    print(f"{n} is equal to zero..")

# 2)Odd or Even
num = int(input("Enter a number:"))
if num%2==0:
    print(f"{num} is a even")
else:
    print(f"{n} is a odd")

# 3)Eligible for vote
age = int(input("Enter your age:"))
if age>=18:
    print("You can vote now!")
else:
    print("You are not eligible")

# 4)greatest of two numbers
num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
if num1>=num2:
    print(num1)
else:
    print(num2)

# 5)Marks
Marks = int(input("Enter Your Marks:"))
if Marks>=90:
    print("Grade A")
elif Marks<=89 and Marks>=75:
    print("Grade B")
elif Marks<=74 and Marks>=60:
    print("Grade C")
elif Marks<=59 and Marks>=40:
    print("Grade D")
elif Marks>40:
    print("Fail")
else:
    print("Please enter valid marks..!")

# 6)weeks
user = int(input("enter a number from 1-7:"))
if user==1:
    print("MONDAY")
else:
    if user==2:
        print("TUESDAY")
    else:
        if user==3:
            print("WEDENSDAY")
        else:
            if user==4:
                print("THURSDAY")
            else:
                if user==5:
                    print("FRIDAY")
                else:
                    if user==6:
                        print("SATURDAY")
                    else:
                        if user==7:
                            print("SUNDAY")

# 7)Simple Calculator
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

# 8)display the name of a month based on the month number (1 for January, 2 for February, etc.).
month_number = int(input("Enter the no.of month:"))
if month_number == 1:
    print("JANUARY")
else:
    if month_number == 2:
        print("FEBRUARY")
    else:
        if month_number == 3:
            print("MARCH")
        else:
            if month_number == 4:
                print("APRIL")
            else:
                if month_number == 5:
                    print("MAY")
                else:
                    if month_number == 6:
                        print("JUNE")
                    else:
                        if month_number==7:
                            print("JULY")
                        else:
                            if month_number==8:
                                print("AUGUEST")
                            else:
                                if month_number==9:
                                    print("SEPTEMBER")
                                else:
                                    if month_number== 10:
                                        print("OCTOBER")
                                    else:
                                        if month_number == 11:
                                            print("NOVEMBER")
                                        else:
                                            if month_number == 12:
                                                print("DECEMBER")

# Medium conditionl statements questions:
# 1) greatest of three numbers:
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = float(input("Enter the third number:"))
if a>=b and a>=c:
    print(f"{a} is the greatest number")
elif b>=a and b>=c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

# 2)Chek year is a leap year or not
year = int(input("enter a year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 3)classify a character entered by the user as a vowel, consonant, or neither. 
consonants = ['b','c','d','f','g','h','j','h','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
character = input("enter a character:").lower()
if character in vowels:
    print(f"{character} is a vowel")
elif character in consonants:
    print(f"{character} is a consonant")
else:
    print("It is not a alphabet..!")
#               or
ch = input("enter  a character").lower()
if len(ch)>1 or len(ch)==0:
    print("Invalid input")
else:
    if ch in 'aeiou':
        print('Vowels')
    elif ch.isalpha():
        print('consonents')
    elif ch.isnumeric():
        print("Number")
    else:
        print("A Special Character")

# 4)Grade -  1.  90-100  : Grade A ,  2.  80-89  : Grade B,  3.  70-79  : Grade C,  4.<70  : Fail.
grade = int(input("Enter your marks:"))
if grade<=100 and grade>=90:
    print("Grade A")
else:
    if grade<=89 and grade>=80:
        print("Grade B")
    else:
        if grade<=79 and grade>=70:
            print("Grade C")
        else:
            if grade<70:
                print("Fail")

# 5) proper triangle
ta = float(input("Enter the 1st angle:"))
tb = float(input("Enter the 2nd angle:"))
tc = float(input("Enter the 3rd angle:"))
total_area=ta+tb+tc
if total_area==180:
    print("It is a valid triangle..!")
else:
    print("It is not a valid traingle..!")

# Loops[easy]:-

# 1) Print all numbers from 1 to 100 using a  for  loop.
for i in range(1,100):
    print(i)

# 2) Write a program to print the sum of the first  n  natural numbers 
no_of_naturals = int(input("Enter the number:"))
total =0
for i in range(1,n+1):
    total+=i
print(f"Sum of natural numbers={total}")
          #or
n = int(input("Enter the number:"))
for i in range(1, n+1):
     summ =  n*(n+1)// 2
print(summ)

# 3)  Print all even numbers between 1 and 50 using a  while loop.
predefined = 1
while predefined<=50:
    if predefined%2==0:
        print(predefined)
    predefined+=1

# 4)display the multiplication table of a given number. First 20
table = int(input("Enter the number:"))
for q in range(1,20):
    print(table, 'X', q, '=', table*q)

# 5)Reverse a number using a  while  loop. and Also can we get the sum of all the digits. 
digits = int(input("Enter a number"))
reversed = 0
while digits > 0:
    last_digit = digits%10 #if any digit that % 10 it results the last digit only
    reversed = reversed*10+last_digit
    digits = digits//10 #if you want to remove the last digit from the given digit use given digit//10 the floor division is used in two ways eliminates the digits after float point and eliminates last digit ffrom given digit
print(reversed)

# 6)Write a program to count the number of digits in a given number using a  while  loop. 
n = int(input("enter a number:"))
count = 0
while n!=0:
    count+=1
    n=n//10
print(count)

# 7)Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop.
positive = True
while positive:
    users = int(input("enter a number:"))
    if users<0:
        positive=False


#Loops Medium
# 1) Print the first 10 terms of the Fibonacci series using a  for loop. 
start_point = 0
end_point = 1
for i in range(start_point,11):
    next = start_point+end_point
    start_point = end_point
    end_point = next
    print(next)

# 2)Check if a given number is a prime number using a  for loop. 
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


# 3)Write a program to calculate the factorial of a number using a  while  loop
import math
factorial_num = int(input("Enter a number:"))
while factorial_num!=0:
    print(math.factorial(factorial_num))
           
        #or(manual way)

fact = 1
y = 1
factor_num = int(input("Enter a num:"))
while fact<=factor_num:
    fact  = fact*y
    y+=1
print(fact)


# 4)Print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop. 
for i in range(1,101):
    if (i%3==0) and (i%5==0):
            print(i)

# 5)Implement a menu-driven program where the user can choose to: 
#    1.  Find the square of a number. 
#    2.  Find the cube of a number. 
#    3.  Exit. 
buzz = True
while buzz:
    menu = input("\nEnter your choice:\n1 = Square of a number\n2 = Cube of a number\n3 = Exit\nYour choice: ").lower()
    entry_num = int(input("Enter a number:"))
    if menu == 1 or menu=="square":
        print(entry_num**2)
    elif menu == 2 or menu=="cube":
        print(entry_num**3)
    elif menu == 3 or menu=="exit":
        print("Exiting..!")
        buzz==False
    else:
        print("You entered invalid input!")

# 6)Implement a basic login system where the user has three attempts to enter the correct password using a loop.
n = int(input("Enter a number:"))
password = "79954"                                                                                                                                                   
attempts = 3
while attempts>0:
    user = input("Enter the password")
    if user == password:
        print("you successfully login")
    else:
        attempts-=1
        print(f'Wrong Password you have only {attempts} attempts')

