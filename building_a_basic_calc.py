"""Objective: Take 2 numbers from a user and add them together.
Then, print the answer out on the screen. PS going to talk abt getting numbers from users, not just strings."""


print("Incorrect Version: ")
num1 = input("Enter a number: ") #python is automatically going to turn the input into a string. Doesn't matter if it's a number.
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

print("Correct Version for Integers: ")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2) #Use int method to convert a string into a number

print(result)

print("Correct Version for All Numbers: ")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) #Use float method to convert a string into a number

print(result)