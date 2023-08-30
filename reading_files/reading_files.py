"""Objective: using the python read command to read a
file that's stored outside of your python file. Remember to always close a file after you open it."""

#open(the file, the mode of opening the file)
#open("employees.txt", "r") # r = read: just want to read info inside the file. Don't want to modify it

#open("employees.txt", "w") # w = write: change the file, you can write info

#open("employees.txt", "a") # a = append: append info onto the end of the file, so you can't modify any of the info in the file. you can add, but not change

#open("employees.txt", "r+") # r+ = read and write: all the power of reading and writing

employee_file = open("employees.txt", "r") #opening a file

#use this line of code before hand
#print(employee_file.readable()) #returns a boolean value that tell us whether or not we can READ (not including write or append) from this file

#print("This spits out the entire file")
#print(employee_file.read()) #this spits out all the info in the file


'''

This prints out each line individually. Less desired way
#this can read each line and imagine it moves the cursor on the file down after each line of code
print(employee_file.readline()) #first line
print(employee_file.readline()) #seconf line
print(employee_file.readline()) #third line

'''

#print(employee_file.readlines()) #this puts all the info in the file into a LIST
#print(employee_file.readlines()[1]) #do this to get specific element in the LIST

for employee in employee_file.readlines():
    print(employee)



employee_file.close() #closing a file