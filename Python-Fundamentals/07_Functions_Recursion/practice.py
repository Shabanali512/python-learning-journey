# -----------------------------
# 1. Print length of list
# -----------------------------

cities = ["Lahore", "Karachi", "Faisalabad", "Sialkot", "Islamabad"]

def print_len(items):
    print("Length of list:", len(items))

print_len(cities)


# -----------------------------
# 2. Print list in single line
# -----------------------------

def print_list(items):
    for item in items:
        print(item, end=" ")
    print()

print_list(cities)


# -----------------------------
# 3. Factorial using loop
# -----------------------------

def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial:", cal_fact(6))


# -----------------------------
# 4. USD to PKR converter
# -----------------------------

def converter(usd):
    pkr = usd * 250
    return pkr

print("1 USD =", converter(1), "PKR")


# -----------------------------
# 5. Even or Odd
# -----------------------------

def check_num(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

print(check_num(5))


# -----------------------------
# 6. Recursive sum of natural numbers
# -----------------------------

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n - 1) + n

print("Sum:", cal_sum(5))


# -----------------------------
# 7. Recursive print list
# -----------------------------

def recursive_print(items, idx):
    if idx == len(items):
        return
    print(items[idx], end=" ")
    recursive_print(items, idx + 1)

recursive_print(cities, 0)
