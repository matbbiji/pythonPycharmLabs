"""Tuple: A type of data structure. Which basically means it's a container that
can store different values. It's very similar to a list, however has key differences (using parenthesis vs bracket)"""

#Tuples are immutible. Meaning they cannot be changed or modified
coordinates = (4, 5) #This is my tuple with coordinates inside of it. ONLY difference from lists are the parenthesis. Whereas, lists use brackets
#THIS WOULDN'T WORK -> coordinates[1] = 10. creates an error
print(coordinates[1])

"""Use tuples over lists for data that will never change. That's why someone is 
probably going to use a tuple for coordinates bc it's never going to change"""

"""Creating a LISTS of Tuples"""

coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[1])

coordinates[2] = 10
print(coordinates[2])