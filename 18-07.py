no_of_units = float(input("Enter the no.of units:"))
bill = 0
if no_of_units>=300:
    bill = no_of_units*4
    print(f"{bill} is your total electricity bill")
else:
    if no_of_units<300 and no_of_units>=200:
        bill = no_of_units*3
        print(f"{bill} is your total electricity bill")
    else:
        if no_of_units<200 and no_of_units>=100:
            bill = no_of_units*2
            print(f"{bill} is your total electricity bill")
        else:
            if no_of_units<100:
                print(f"{bill} is your total electricity bill")

# Accurate code
units = float(input())
if units<100:
    print("No current bill")
else:
    if units<=200:
        print(units*2)
    else:
         if units<=300:
             print(units*3)
         else:
             if units<=400:
                 print(units*4)
             else:
                 print(units*5)

# Iteration Statements(Looping Statements) => 

