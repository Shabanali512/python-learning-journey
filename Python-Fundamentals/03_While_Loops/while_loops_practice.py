# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


# Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1


# Multiplication table of a number
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# Print elements of a list
numbers = [1, 4, 9, 8, 52.64, 58, 3]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# Search for a number in a tuple
nums = (1, 4, 9, 8, 52.64, 58, 3)
x = 3
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
    i += 1


# Using break
nums = (1, 4, 9, 8, 52.64, 58, 3)
x = 9
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1


# Using continue
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
