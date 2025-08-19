n = 25
for i in range(0, n):
    print(i)

#Even numbers
for i in range(0,20,2):
    print(i)
      #or
for i in range(0,20):
    if i%2 == 0:
        print(i)
        
#Odd numbers 
for i in range(0,20):
    if i%2!=0:
        print(i)
        #or
for i in range(1,20,2):
    print(i)


for i in range(1,100):
    if i in range(40,50):
        print(i)
    if i in range(70,80):
        print(i)
        #or
for i in range(1,100):
    if(i>=40 and i<=49):
        print(i)
    elif(i>=70 and i<=79):
        print(i)
        #or
for i in range(1, 100):
    if (40<=i<=49) or (70<=i<=79):
        print(i)

n = int(input("Enter a number:"))
for i in range(1,11):
    print(n, 'X', i, '=', n*i )