# -----------------------------
# 1. Create and read a file
# -----------------------------

filename = "practice_file.txt"

with open(filename, 'w') as f:
    f.write("Hi, this is python fundamental file")

with open(filename, 'r') as f:
    content = f.read()
    print(content)


# -----------------------------
# 2. Create practice.txt file
# -----------------------------

filename = "practice.txt"

with open(filename, 'w') as f:
    f.write("Hi everyone\n")
    f.write("we are learning file i/o\n")
    f.write("using java\n")
    f.write("I like programming in java\n")

with open(filename, 'r') as f:
    content = f.read()
    print(content)


# -----------------------------
# 3. Replace "java" with "python"
# -----------------------------

with open(filename, 'r') as f:
    content = f.read()

new_content = content.replace("java", "python")

with open(filename, 'w') as f:
    f.write(new_content)

print("\nAfter replacing:")
print(new_content)


# -----------------------------
# 4. Search word in file
# -----------------------------

with open(filename, 'r') as f:
    content = f.read()

if "learning" in content:
    print("Word Found")
else:
    print("Word Not Found")


# -----------------------------
# 5. Find line number of word
# -----------------------------

def check_line(word):
    line_no = 1
    with open(filename, 'r') as f:
        for line in f:
            if word in line:
                return line_no
            line_no += 1
    return -1

print("Line number:", check_line("learning"))


# -----------------------------
# 6. Count even numbers from file
# -----------------------------

# Example numbers.txt content:
# 1,2,3,4,5,6,7,8

count = 0

with open("numbers.txt", 'w') as f:
    f.write("1,2,3,4,5,6,7,8")

with open("numbers.txt", 'r') as f:
    data = f.read()
    numbers = data.split(",")

    for num in numbers:
        if int(num) % 2 == 0:
            count += 1

print("Even numbers count:", count)
