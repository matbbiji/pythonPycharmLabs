"""Function: a collection of code which performs a specifc task. it allows you
to break up your code"""

'''After the colon, all the code is in that function/is outputted'''
def say_hi(name, age): #just have to state the name of the thing you want in the parameter
    print("Hello " + name + ", you are " + age) #to have code inside the function, it needs to be indented

'''You need to call the function to see anything printed out'''
say_hi("Mike", "35")
say_hi("Steve", "70")

print()
"Using an int or float rather than a string for a number"
def say_hi1(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi1("Mike", 35)
say_hi1("Steve", 70)