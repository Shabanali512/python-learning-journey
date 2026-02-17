# ==============================
# Print elements of a list
# ==============================

numbers = [1, 4, 9, 8, 52.64, 58, 3]
for i in numbers:
    print(i)


# ==============================
# Search a number in tuple
# ==============================

nums = (1, 4, 9, 8, 52.64, 58, 3)
x = 8

for index, value in enumerate(nums):
    if value == x:
        print("Found at index", index)


# ==============================
# Range Examples
# ==============================

for i in range(10):          # range(stop)
    print(i)

for i in range(2, 10):       # range(start, stop)
    print(i)

for i in range(2, 10, 2):    # range(start, stop, step)
    print(i)


# ==============================
# Print 1 to 100
# ==============================

for i in range(1, 101):
    print(i)


# ==============================
# Print 100 to 1
# ==============================

for i in range(100, 0, -1):
    print(i)


# ==============================
# Multiplication Table
# ==============================

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# ==============================
# Sum of n numbers (for loop)
# ==============================

num = int(input("Enter a number: "))
total = 0
for i in range(1, num + 1):
    total += i
print("Total sum:", total)


# ==============================
# Sum of n numbers (while loop)
# ==============================

num = int(input("Enter a number: "))
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print("Total sum:", total)


# ==============================
# Factorial (while loop)
# ==============================

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)


# ==============================
# Factorial (for loop)
# ==============================

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
