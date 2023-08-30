'''
Objective: Catching errors in python. Handling errors and doing things when they occur
'''

'''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")
'''

#example where except print line isnt accurate

'''
a number cannot be divided by 0. so this will throw out an error. 
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except: 
    print("Invalid Input")
    
output: Invalid Input
however, the first error isn't bc of an invalid input
'''

# we can and should catch more specific errors

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # you can create a variable to store the error then print it out
    print(err)
except ValueError:
    print("Invalid Input")