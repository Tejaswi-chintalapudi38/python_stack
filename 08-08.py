# Prime number => any number which has only two factors the 1 and itself that is called as prime numbers

# Posssible Ways:
number = int(input("Enter a number:"))
count = 0
for i in range(1, number+1):
    if i%2==0:
        count+=1

if count == 2:
    print(f"{number} is a prime number")
else:
    print(f"Not a {number} prime number")


# Possible-way2:
num = int(input("Enter a number:"))
flag = True
for i in range(2,num):
    if num%i==0:
        flag = False
        print("It is not aprime number")

if flag==True:
    print("It is a prime number")


def is_prime(num1):
    if num1<1:
        return 'not a prime'
    
    for i in range(2,num1):
        if num1%i==0:
            return 'not a prime'
    
    return 'is prime'

print(is_prime(5))

num1 = int(input("Enter a number:"))
if num1<=1:
    print('not a prime')
else:
    flag = True
    for i in range(2,num1):
        if num1%i==0:
            flag= False
            print("not a prime")
            break
    
    if flag == True:
        print('prime number')
