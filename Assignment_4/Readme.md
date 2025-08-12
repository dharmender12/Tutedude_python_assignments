# Assignment 4 - Module 5: Files, Exceptions, and Errors in Python

## **Overview**
This repository contains Python scripts for:
1. Reading files with error handling.
2. Writing and appending to files, then reading the final content.

---

## Task 1: Read a File and Handle Errors
This program:
- Opens and reads a file named `sample.txt`
- Prints each line of the file
- Handles the error gracefully if the file does not exist

### Example (File Exists)
Reading 'sample.txt'...

Hello World
This is sample content.


### Example (File Missing)

Error: The file 'sample.txt' does not exist.

---

## Task 2: Write and Append Data to a File
This program:
- Takes user input and writes it to a file named `output.txt`
- Appends additional user input to the same file
- Reads and displays the final file content

### Example

Enter data to write into the file: 25
Enter additional data to append: 50

Final content of 'output.txt':

25
50

---

## Files in This Repository
- `task1_read_file.py` → Task 1 solution
- `task2_write_append_file.py` → Task 2 solution
- `README.md` → Documentation file
- `sample.txt` → (Optional) For testing Task 1

