"""Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
# Create a dictionary of student marks
student_marks = { 
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}

## 2. Ask the user to input a student's name
student_name = input("Enter the student's name: ")

## 3. Retrieve and display the corresponding marks

if student_name in student_marks: 
    print(f"{student_name}'s marks: {student_marks[student_name]}")

else: 
    print('Student not found.')
    
