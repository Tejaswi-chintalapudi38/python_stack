#variable-A container for a value(string,integer,float,boolean)
#         A variable behaves as the value that contains

#String-The sequence of characters represented in single-'' or the double quotes @@
first_name="Chintalapudi"
food="Biryani"
print(first_name)

#f-string-->begin a string with f or F before the opening quototion mark or triple  quotation mark
#           inside this string, you can write a python expression between {} that can refer a variables
print(f"Hello {first_name}")
print(f"Your favourite food is {food}")

#Integers-->The whole numbers
age=21
quantity=50
print(f"You are {age} years old and you are buying {quantity} items")

#Float-->The floating point precision and contains decimal point nubers
price=10.99
print(f"The price is {price}")

#Boolean-->represnts the truth values in logical expressions and conditionals it has only two values:True or False
is_student=True
print(f"Are you a student {is_student}")