def number_positive_negative(num):
    return 'positive' if num>0 else 'negative'


def check_even_odd(num1):
    return 'Even' if num1%2==0 else 'odd'

def check_greater(num1,num2):
    print(num1) if num1>num2 else print("both are equal") if num1==num2 else print(num2)

num1, num2, num3 = 10, 4, 6
if num1>num2 and num1>num3:
    print(num1)
elif num2>num3:
    print(num2)
else:
    print(num3)    

def check_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return 'Leap year'
    else:
        return 'Not a leap year' 
    
print(check_year(2004))

def check_year(year):
    return 'Leapyear' if (year%4==0 and year%100!=0) or (year%400==0) else 'Not a Leapyear'

def check_grade(marks):
    if marks>=100 and marks>=90:
        return 'Grade A'
    elif marks<=89 and marks>=80:
        return 'Grade B'
    elif marks<=79 and marks>=70:
        return 'Grade C' 
    else:
        return 'Fail'

s1, s2, s3 = 3, 4, 5
if (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2):
    print('valid triangle')
else:
    print('not a ')


#valid triangle
#type of triangle
#is  a right angle triangle or not by using pythogorous theorems

n = 100
for i in range(1, n+1):
    if i%2==0:
        print(i)
    
for i in range(2, n+1, 2):
    print(i)

start = 1
while start<=100:
    if start%2==0:
        print(start)
    start+=1

start = 2
while start<=100:
    print(start)
    start+=2    

