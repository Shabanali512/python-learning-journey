# 1. Take 5 numbers from user and store in list

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Your list:", numbers)


# 2. Sum of list

total = sum(numbers)
print("Sum of list:", total)


# 3. Maximum number in list

maximum = max(numbers)
print("Maximum number:", maximum)


# 4. Reverse list without reverse()

reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


# 5. Second largest number

sorted_list = sorted(numbers)
second_largest = sorted_list[-2]
print("Second largest number:", second_largest)
