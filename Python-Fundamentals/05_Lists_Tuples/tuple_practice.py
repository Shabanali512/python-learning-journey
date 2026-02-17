# 1. Create a tuple

numbers = (10, 20, 30, 40, 20, 10)

print("Tuple elements:")

for num in numbers:
    print(num)


# 2. Count how many times 20 appears

count_20 = numbers.count(20)
print("20 appears", count_20, "times")


# 3. Find index of 30

index_30 = numbers.index(30)
print("Index of 30:", index_30)
