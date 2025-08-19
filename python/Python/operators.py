# Arithmetic operators-->Mathematical operations such as +, -, *, /, //, %, **
a = 10
b = 3
c = 3.14
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Assignment operators-->used to represent assigning a value using'='
print("\nAssignment Operators:")
a = 5
print("a =", a)
a += 5
print("a += 5, a =", a)
a -= 3
print("a -= 3, a =", a)
a *= 2
print("a *= 2, a =", a)
a /= 4
print("a /= 4, a =", a)
a %= 2
print("a %= 2, a =", a)
a **= 3
print("a **= 3, a =", a)
a //= 2
print("a //= 2, a =", a)

# Comparison operators-->are used to compare two values
x = 8
y = 5
print("\nComparison Operators:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Logical operators-->the 'and' opertor are used to 
p = True
q = False
print("\nLogical Operators:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# Bitwise operators
m = 10  # Binary: 1010
n = 3   # Binary: 0011
print("\nBitwise Operators:")
print("m & n:", m & n)
print("m | n:", m | n)
print("m ^ n:", m ^ n)
print("~m:", ~m)
print("m << 2:", m << 2)
print("m >> 2:", m >> 2)

# Membership operators
list1 = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print("3 in list1:", 3 in list1)
print("6 not in list1:", 6 not in list1)

# Identity operators
r = "hello"
s = "hello"
print("\nIdentity Operators:")
print("r is s:", r is s)
print("r is not s:", r is not s)

