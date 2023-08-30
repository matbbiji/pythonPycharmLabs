"""Objective: Take an input from the user. Store the input into a variable.
 And then use the stored information."""


'''input() = pretty much tells python that we want to get input from the user. you can add a prompt into the parameter'''
name = input("Enter your name: ") #store the input value into the name variable
print("Hello " + name + "!")
print()

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
