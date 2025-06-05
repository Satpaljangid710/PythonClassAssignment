"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

# Answer
n1 = input("Enter first number:", )
n2 = input("Enter second number: ")
n1 = int(n1)
n2 = int(n2)

# Addition
print("Addition:", n1 + n2)
# Subtraction
print("Subtraction:", (n1 - n2))

# Multiplication
print("Multiplication:", (n1 * n2))

# Division
print("Division:", n1 / n2)
