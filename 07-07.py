#1. Add an integer and float. What is the result’s type?
a = 10
b = 13.4
print(a+b) # The result is a float value


#2.	Create a string and access its:
Str = "Tejaswi Chintalapudi"
 # First character
print(Str[0])
 #Last character
print(Str[-1])
 #A substring from index 2 to 5
print(Str[2:6])


#3.	Concatenate two strings and print the result.
name1 = "Mani"
name2 = "Chintalapudi"
print(name1+" "+name2)


#4.	Define list. What are the difference between List(mutable, contain duplicates) and Tuple(immutable, can contain duplicates).
list1 = ["Divya", 28, "Sravani", 34, "Sai", 23, 28]
print(list1)
list1[2] = "Ammulu"
print(list1)
tuple1 = ("Divya", 28, "Sravani", 34, "Sai", 23, 28)
print(tuple1)
#tuple1[2] = "Teju"
print(tuple1)


#5.	Write a programme to print a list in reverse order.
list2 = ["Mani",19, "Nani", 17, "Sai", 15]
print(list2[::-1])


#6.	Create a tuple of 4 elements. Print the first and last element.
tuple2 = ("joy", "dolly", 10, 21)
print(tuple2[0])
print(tuple2[-1])
#7.	Try changing a value in a tuple. What happens?
#tuple2[1] = "varshitha"
#print(tuple2)


#8.	Create a dictionary of 3 students with their marks. Print the dictionary.
dict1 = {"student1": 96,
         "student2": 78,
         "student3": 30}
print(dict1)
#9.	Access the marks of one student using their name.
print(dict1["student2"])
#10.	Update the marks of an existing student.
dict1["student2"] = 75
print(dict1)


#11.	Can I access a key using a value in a dictionary - No beacuse the value can duplicate but the keys are mustbe unique
 #In Python, a dictionary is a collection of key-value pairs where each key must be unique.
 #This means that you cannot have duplicate keys in a dictionary. 
 #If you attempt to add a duplicate key, the new value will overwrite the existing value associated with that key.


#12.	 Can I have duplicate values and keys in a dictionary? What happens if I wanted try to duplicate key in a dictionary? 
dict2 = {"student1": 96,
         "student2": 78,
         "student3": 30,
         "student1": 92} #Keys: Must be unique; duplicate keys will overwrite the previous value.
print(dict2)             #Values: Can be duplicated; multiple keys can have the same value.


#13.	Print all multiples of 17 using range. Numbers should start from -34 and end below 400
 #range is used to compute the sequence of numbers
print(list(range(-34, 400, 17)))
