#Basic:

#print numbers from 1 to 11
for i in range(1,11):
    print(i)

#print  even numbers from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)
    
#print  odd numbers from 1 to 20
for i in range(1,21):
    if i%2!=0:
        print(i)
    
#Print multiplication table of 5
n = int(input("Enter the number:"))
table = 5
for i in range(1,n+1):
        print(f"{table} X {i} = {table*i}")

#Print squares of numbers from 1 to 10
for i in range(1,11):
     print(i**2)