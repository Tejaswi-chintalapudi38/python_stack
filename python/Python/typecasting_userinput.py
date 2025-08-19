#Typecasting-->the process of converting a variable from one datatype to another
#              str(), int(), float(), bool()
name="Tejaswi Chintalapudi"
age=21
gpa=72.1
is_graduate=True
age=str(age)
print(type(age))
name=bool(name)
print(name)

#input()-->A function that prompts the user to enter data and returns the entered data as a string
name=input("What is your name:")
print(f"Hello {name}")
age=int(age)
age+=1
this_year=int(input("How old are you:"))
print(f"You are {age} old now!")

#Area of Rectangle:
length=float(input("Enter length value:"))
width=float(input("Enter width value:"))
Area=width*length
print("The Area of rectangle is {Area}cm")

#Shopping cart program
item=input("what item would you like to buy?")
price=float(input("What is the price:"))
quantity=int(input("How many would you like?"))
total=price*quantity
print(f"You have bought{quantity} x {item}/s")
print(f"Your total is:${total}")

#Madlibs game
adjective1=input("Enter an adjective (description): ")
noun1=input("Enter a noun(person,place,thing): ")
adjective2=input("Enter an adjective (description): ")
verb1=input("Enter a verb ending with 'ing'")
adjective3=input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a{noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")



