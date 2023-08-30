from math import * #need to write this line of code in order to access libraries with more math functions
"This is called a module and the math module gives access to more math functions"

print(3 * 4 + 5) #follows PEMDAS rules
print(3 * (4 + 5))
print(2.04949)
#modules operator
print(10 % 3) #remainder is 1 after dividing 10 by 3

'''can literally do anything within the print statement'''
print()
my_num = 5
print(my_num)
print()

print("Converting a number into a string\n--------------------")
num1 = 6
print(str(num1)) #this outputs a string, not a num.

'''str() comes in handy when you want to print out numbers alongside strings'''

print(str(num1) + " is my favorite number")

print()
print("Functions Related to Numbers\n--------------------\n")
my_num2 = -5
print("Absolute Function/Method: ")
print(abs(my_num2)) #abs method: gives absolute number
print("Power Function/Method:")
print(pow(3, 2)) #outputs answer to 3^2
print("Maximum Function/Method:")
print(max(4, 6)) #outputs bigger of the 2 numbers in the parameter
print("Minimum Function/Method:")
print(min(4, 6)) #outputs smaller of the 2 numbers in the parameter
print("Round Function/Method:")
print(round(3.2)) #outputs rounded number
print("Floor Function/Method:")
print(floor(3.7)) #outputs rounded down number
print("Ceiling Function/Method:")
print(ceil(3.7)) #outputs rounded up number
print("Square Root Function/Method:")
print(sqrt(36)) #outputs the square root of the number inputted