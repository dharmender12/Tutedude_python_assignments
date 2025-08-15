"""
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""

## Create a list of numbers from 1 to 10.

numbers = list(range(1, 11))


## Extract the first five elements from the list.
first_five_numbers = numbers[:5]

## Reverse these extracted elements

reversed_five_num = first_five_numbers[::-1]

## Printing extracted and reversed list 
print(f"Original list: {numbers}")
print(f"Extracted first five elements: {first_five_numbers}")
print(f"Reversed extracted elements: {reversed_five_num}")