# ==============================
# Even or Odd Checker
# ==============================
num=int(input("Enter a number :"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")


# ==============================
# Largest of Two Numbers
# ==============================
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1>num2:
    print("First number is largest")
elif num1==num2:
    print("Both numbers are equal")
else:
    print("Second number is largest")


# ==============================
# Largest of Three Numbers
# ==============================
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)


# ==============================
# Simple Login System
# ==============================
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# ==============================
# FizzBuzz Program
# ==============================
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
