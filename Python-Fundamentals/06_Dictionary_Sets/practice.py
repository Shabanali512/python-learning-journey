# -----------------------------
# 1. Store word meanings in dictionary
# -----------------------------

my_dict = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}

print("Dictionary:", my_dict)
print("Type:", type(my_dict))


# -----------------------------
# 2. Count classrooms required
# -----------------------------

subjects = {"python", "java", "c++", "python", "javascript",
            "java", "python", "java", "c++", "c"}

print("\nSubjects:", subjects)
print("Type:", type(subjects))
print("Number of classrooms needed:", len(subjects))


# -----------------------------
# 3. Store marks in dictionary
# -----------------------------

marks = {}

x = int(input("\nEnter marks of python: "))
y = int(input("Enter marks of java: "))
z = int(input("Enter marks of c++: "))

marks["python"] = x
marks["java"] = y
marks["c++"] = z

print("Student Marks:", marks)


# -----------------------------
# 4. Store 9 and 9.0 separately
# -----------------------------

values = {9, 9.0}

print("\nSet with 9 and 9.0:", values)
