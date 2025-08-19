# Nested Loops
#count = 0
#for class_no in range(1,11):
#    for roll_no in range(1, 31):
#        count+=1
#        print(f"Class {class_no} roll {roll_no}")
#print("No of times that can be iterated:",count)

#for table in range(1,13):
#    for table_end in range(1,21):
#        print(table, "X", table_end, '=', table*table_end)

#for class_no in range(1,11):
#    for roll_no in range(1, 31):
#       if roll_no%2 == 0:
#            print(f"Class {class_no} roll {roll_no}")

#for class_no in range(1,11):
#    if class_no%2 == 0:
#        for roll_no in range(1, 31):
#                print(f"Class {class_no} roll {roll_no}")
            
#for class_no in range(1,11):
#    if class_no%3 == 0:
#        for roll_no in range(1, 31):
#            if roll_no%7 == 0:
#                print(f"Class {class_no} roll {roll_no}")

#for class_no in range(1,11):
#    for roll_no in range(1, 31):
#        if class_no%2 == 0 and roll_no%7 == 0:
#            print(f"Class {class_no} roll {roll_no}")

class_no = 1
while class_no<=10:
    roll_no = 1
    while roll_no<=31:
        print('class', class_no, 'roll', roll_no)
        roll_no+=1
    class_no+=1
    
        