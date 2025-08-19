# Lambda Function : are the anonymous function(even when you define the lambda function with a variable whenever changes that variable the total lambda function will be collapsed  )
#                   In lambda function we will write n no.of parameters but we write one expression only
#                   The lambda functions are non-void functions(without explicitely writing the return statement it automatically defines the return statement in lambda function) mainly used in higher order functions
operation = lambda a, b, c, d:a+b-c*d
print(operation(5, 4, 2, 8))



# Higher_Order Function: the functions that takes function and arguments as arguments 

# Map => map(function,iterable)
def square(x):
    return x**2

print(list(map(lambda x:x**3,[3, 4, 5, -32, 11])))
print(list(map(square,[5, 6, -25, 3])))

# Filter => filter(function, iterable)
print(list(filter(lambda x:x%2==0, [1,8,5,2,9])))

print(list(filter(lambda x:x>5, [1,7,3,4,9])))
print(list(filter(lambda x:x%5==0 or x%3==0, [1, 3, 5, 8, 9, 10, 15, 17])))

from functools import reduce
print(reduce(lambda x, y:x+y, [1, 2, 8, 5, 7, 11, -10]))
print(reduce(lambda x,y: x if x>y else y, [12, 15, 2, 5,8]))
print(reduce(lambda x,y: x if x<y else y, [12, 15, 2, 5,8]))

def check(n):
    if n%2==0:
        return True
    return False