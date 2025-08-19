# Jumping Statements => Jump statements in Python are used to alter the normal flow of program execution, primarily within loops and functions. 
#                         i) break => Terminates the current loop (either for or while) immediately.
#                         ii) continue => Skips the rest of the current iteration of a loop.
#                         iii) pass => Acts as a null operation; it does nothing.

for i in range(1,100):
    print(i)
    if i == 50:
        break

for j in range(1000):
    print(j)
    if j == 8:
        break
    print(j)
    print(j)

for c in range(1,25):
    print(c)
    if c == 8:
        continue
    print(c)
    print(c)

for m in range(1, 32):
    if m < m * (-1):
        continue
    print(m ** 2)

for class_no in range(1, 11):
    for roll_no in range(1, 31):
        if roll_no == 5:
            break
        print(class_no, roll_no)
    
for class_no in range(1, 11):
    for roll_no in range(1, 31):
        if roll_no == 5:
            continue
        print(class_no, roll_no)

for class_no in range(1, 11):
    for roll_no in range(1, 31):
        if roll_no > 5 or roll_no < 16:
            break
        print(class_no, roll_no)
    
num1 = int(input("Enter a number:"))
if num1%2==0:
    pass
