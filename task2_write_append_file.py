"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

filename = "output.txt"

with open(filename, "w") as file:
    user_input = input("Enter text to write to the file:  ")
    file.write(user_input + "\n")
    print(f"Data successfully written to {filename}.")
print("\n")
print("\n")
with open(filename, "a") as file:
        inp = input("Enter additional text to append: ")
        file.write(inp + "\n")
        print(f"Data successfully appended.")

print("\n")
print("\n")
print(f"Final content to {filename}:")
print("\n")

with open(filename,mode='r') as file: 
    for line in file:
        print(line)

print("\n")
