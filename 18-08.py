#The preference order of the function scopes are: local > enclosed > global > built-in 
num = 10
def check_function():
    num2=20  
    def inner_function():
        num2=50 #the num2 is created and accessed by inner_function only
        print(num2)
    inner_function()
    print(num2)

check_function()
print(num)

#We have to change the global variable neigther creating another varaiable in localscope by using global keyword
num3 = 10
def first_function():
    num2 = 22
    global num3
    num3 = 40
    print(num3)

first_function()
print(num3)
    


num1 = 10
def preference():
    num1 = 20
    globals()['num1'] = 50
    print(num1)

preference()
print(num1)


# To change the enclosed scope variable by using nonlocal keyword
num4 = 10
def first_function():
    num4 = 20 
    def second_function():
        num4 = 20
        def third_function():
            nonlocal num4
            num4 = 30
            print(num4)
        third_function()
        print(num4)
    second_function()

first_function()
print(num4)

#scope generally says which area we can access that variable
#lifetime generally how much time it can be accessed

#lambda function can have only one expression
# we don't have to write the return explicitely
