def simple_calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    if b!=0:
        print(a/b)
        print(a%b)
        print(a//b)
    else:
        print("Division not possible")

# POSITIONAL ARGUMENTS
simple_calc(5,6)

# KEYWORD ARGUMENTS
simple_calc(b=9, a=15)

# POSITIONAL + KEYWORD
simple_calc(5, b =10)
# We can't write like this simple_calc(b=10, 5) it leads to the error because we can't write keyword arguments before positional arguments
# It leads to the error:- positional argument follows keyword argument


#DEFAULT ARGUMENTS:
def simple_calc(a,b=30): 
    print(a+b)
    print(a-b)
    print(a*b)
    if b!=0:
        print(a/b)
        print(a%b)
        print(a//b)
    else:
        print("Division not possible")
    
simple_calc(a=5, b=13) 
simple_calc(6)
# You can't mention default arguments before non-default arguments 
#  def simple_calc(a=3,b): it leads an error 
#  the error should be SyntaxError: parameter without a default follows parameter with a default


def add(a,b):
    print(a+b)

def add(a,b,c):
    print(a+b+c)

def add(a,b,c,d):
    print(a+b+c+d)

add(2,3)# It results: TypeError: add() missing 2 required positional arguments: 'c' and 'd'

# It called as Method Overloading - same function name for diffrent methods 
# The python does not supports the method overloading so it just ignores evry method and just treat last method as the actual one
# So in this case we use arbitary arguments can be introduced

# ARBITARY ARGUMENTS : It can any no.of arguments
def add(a, *b):
    print(a+b)

add(4, 6, 7) # the a should be taken one parameter then b works on any no.of arguments
add(4, 6, 1, 2, 4)