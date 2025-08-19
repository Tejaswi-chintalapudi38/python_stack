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

simple_calc(5,6)
simple_calc(8,9)
simple_calc(12,5)