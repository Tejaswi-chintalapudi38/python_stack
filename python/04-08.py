# adding # Basically the arbitary arguments stored in the form of tuple
def add(a, *b):
    temp = a
    for i in b:
        temp+=i
    print(temp)

# *args => arbitary arguments
# **args => Keyword arbitary arguments => casually everyone mention the keyword arguments as **kargs
# KEYWORD ARGUMENTS: we can associate key to a value as like the keyword arguments stored the values in the form of key-value pairs
def connect_to_db(**kargs):
    print(kargs)
    print(type(kargs))

connect_to_db(db_loc = "localhost:3300", db_pool = 234, db_password = '23344')

def connect_to_db2(*args):
    print(args)
    print(type(args))

connect_to_db2("localhost:3300", 234, '23344')

# RETURN KEYWORD: returning a value from function even after the task completion 
#  one return statement can contain multiple values
#  return statement once executed can be considered as end of the function call        
#  any function without using return keyword that function is called as void functions

def func(a):
    if a%2==0:
        return 'even'
    else:
        return 'odd'
    
print(func(5))

def sum_of_natural(n):
    count = 0
    for i in range(1,n+1):
        count+=i
    return count

print(sum_of_natural(5))

def simple_calc(a, b):
    return a+b, a-b, a*b, a/b

print(simple_calc(4,5))


def simple_calc(a,b):
    return a+b
    return a-b # the code should be structurally not reachable because if the return statement once hit the next line of code cannot be exceuted in this case the return statement acts as a stoppoint
    return a*b
print(simple_calc(2,4))

def check(n):
    for i in range(1,n):
        print(i)
        if i == 9:
            return
    return 55

print(check(22))