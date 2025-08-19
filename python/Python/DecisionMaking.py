#if = Do some code only if some conditions is True
#      Else do something

age=int(input("Enter Your Age:"))

if age>=100:
    print("You are too old to signup!")
elif age>=18:
    print("You are now signed up!")
elif age<0:
    print("You haven't born yet!")
else:
    print("You must be 18+")
    
online=True
if online:
    print("User is Online")
else:
    print("User is Offline")

#Calculator
operator=input("Enter Which Operation To Be Performed(+, -, *, /, %):")
num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2nd number:"))

if operator=="+":
    result=num1+num2
    print(round(result, 3)) #round function is used display the nearest integer of result and it displays only 3decimal places
elif operator="-":
    result=num1-num2
    print(round(result, 3))
elif operator="*":
    result=num1*num2
    print(round(result, 3))
elif operator="/":
    result=num1/num2
    print(round(result, 3))
elif operator="%":
    result=num1%num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid")
    


# Weight Converter
weight=float(input("Enter your weight"))
unit=input("Kilogram or Pounds? (K or L)")
if unit=="K":
    weight=weight*2.205
    unit="Lbs"
elif unit=="L":
    weight=weight/2.205
    unit="Kgs"
else:
    print(f"{unit} was not valid")
print(f"Your weight is : {round(weigt, 1)} {unit}")


# Temperarture conversion
unit=input("Is this temperature in celsius or fahrenheit(C/F)")
temp=float(input("Enter the temperature: "))

if unit=="C":
    temp=round((9*temp)/5+32, 1)
    print("The temperature in Fahrenheit is: {temp}F")
elif unit=="F":
    temp=round((temp-32)*5/9, 1)
    print("The temperature in Fahrenheit is: {temp}C")
else:
    print(f"{unit} is an invalid unit")
    


