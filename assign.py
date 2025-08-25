def vowel_check(str):
    count = 0
    vowels = 'aeiouAEIOU'
    for n in vowels:
        if n in str:
            count+=1
    print(count)

vowel_check("Tejaswi")


def remove_duplicates_sort(arr):
    unique = []
    for num in arr:
        if num not in unique:   
            unique.append(num)
    n = len(unique)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]
    return unique
arr = ['z', 'a', 'p', 'c', 'a', 'z', 'k', 'n', 'c']
print("After:",remove_duplicates_sort(arr))


n = int(input("Enter a number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()


def pyramid(n):
    for i in range(1, n + 1):  
        print(" " * (n - i), end="")  
        for j in range(1, i + 1):
            print(j, end=" ")
        print() 
pyramid(5)
