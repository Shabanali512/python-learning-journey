# Day 8 - File Input/Output (File I/O)

## 📌 Topics Covered

- What is File Handling?
- open() function
- File Modes (r, w, a)
- read(), write(), readline()
- replace() in file
- Searching word in file
- Counting even numbers from file

---

# 🔹 What is File I/O?

File I/O means reading data from a file and writing data into a file.

Syntax:

open("filename", "mode")

Modes:
r  -> read
w  -> write (overwrites file)
a  -> append
r+ -> read and write

---

# 🔹 Important Methods

f.read()        -> reads entire file  
f.readline()    -> reads one line  
f.write()       -> writes data  
f.close()       -> closes file  

Using with statement is recommended:

with open("file.txt", "r") as f:
    data = f.read()

---

# 🚀 Practice Programs Included

✔ Create and read file  
✔ Write multiple lines  
✔ Replace word in file  
✔ Search word in file  
✔ Find line number of word  
✔ Count even numbers from file  

---

🔥 Real-world programming starts here!
