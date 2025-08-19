s = {10, 20, 30, 10, 19}
for n in s:
    print(n)

d = {'name':'aparna', 'p-no': 123}
for n in d.items():
    print(n)

s = 'string'
for n in s:
    print(n)

str = "teju"
for st in str[::-1]:
    print(st)

stri = "teju"
for i in stri:
    print(stri, end=',')

S = 'string'
count = 0
for n in s:
    count+=1
print(count)

n = "hello world"
for i in n:
    if i in 'aieouAEIOU':
        print(i)
    
tt = "hello python"
count = 0
for i in n:
    if i in 'aeiouAEIOU':
        count+=1
        print(count)

l = [10, 20, 667, 8, 9]
for i in l:
    if i%2==0:
        print(i)
    
k = [10, 20, 667, 8, 9]
ecount = 0
ocount = 0
for i in k:
    if i%2==0:
        ecount+=1
    else:
        ocount+=1
print("even number:",ecount)
print("odd number:",ocount)

#ascii => 0 to 127
#0 => none
#A to Z => 65 to 90
#a to z => 97 to 122