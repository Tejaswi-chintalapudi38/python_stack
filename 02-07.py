# Variables - A variable is essentially a storage location in a computer's memory that is given a name, allowing you to refer to the data stored there. 
#             The term "variable" is used because the value it holds is not fixed and can be modified or reassigned throughout a program or calculation. 
# Rules - rules that applies when naming a variable. Some rules :
#         1)Variables name cannot contain spaces.
#         2)A variable name cannot start with a number. can start with a-z or A-Z or _
#         3)A variable name cannot be a reserved word like if, else, for, function etc
# Naming Conventions beacuse the name should convey some meaning, mustly name variables properly
# 3types - snake_case, Camelcase, Pascalcase
#userconfirmpassword => snakecase - user_confirm_password
#                       pascalcase - UserConfirmPassword
#                       camelcase - userConfirmPassword m  nnn, n n
# Assign two numbers to variables `a` and `b`, and print their sum.
a = 3
b = 4
print(a+b)

# A Python program to subtract two numbers and print the result
print(a-b)

# Multiply two variables and store the result in a third variable. Print all three.
c = a*b
print(a)
print(b)
print(c)

# Divide 10 by 3 and print the result with and without decimals
print(10/3)
print(10//3)

# Use floor division `//` to divide 17 by 4. Print the output.
print(17//4)

# Use the modulo operator `%` to check the remainder when 25 is divided by 6.
print(25%6)


# Square of a number
a = 2
b = 6
c = b**a
print(c)


# Assign values to three variables `x`, `y`, `z` and compute the average
x = 5
y = 3
z = 8
print(x + y + z / 2) 


# Take a number and find its cube using the `**` operator.
a = 5
b = 3
print(a**b)


# Area of Rectangle
length = 30
width = 40
area = length*width
print("Area of given rectangle:",area)


# Assign a variable `total_marks = 450` and `obtained_marks = 375`. Find percentage.
total_marks = 450
obtained_marks = 375
print("The percentage is:",total_marks%obtained_marks)


# Write a Python statement that calculates `(a + b) * c` for some values of a, b, and c.
a = 3
b = 7
c = 21
print((a+b)*c)


# Draw and show how reassignment changes variable reference to a memory block.
a = 10
b = 20
print(a+b)
b = 30
print(a+b)

