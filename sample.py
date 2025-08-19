n = int(input("Enter a number:"))
for i in range(2,n):
    if n%i == 0:
        print("It is not a prime number")
    else:
        print("It is a prime number")
    
character = input("enter a character:").lower()
alphabet = character.isalpha()
number = character.isalnum()
if alphabet == True:
    print(f"{character} is a alphabet")
elif number == True:
    print(f"{character} is a number")
elif alphabet == True and number==True:
    print(f"{character} is a combination of both alphabets and numbers")


user_string = input().lower()
count = 0
alphabets = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for user_string in alphabets:
    count+=1
print(count)
