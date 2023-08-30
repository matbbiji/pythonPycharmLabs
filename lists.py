'''Objective: using lists to organize lots of information.'''

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends) #prints entire list
print()
print(friends[0]) #accesses the first friend
print(friends[-1]) #accessing information from the back of the list "Toby"
print(friends[1:]) #prints every index after 1 including 1
print(friends[1:3]) #prints from index 1 all the way up to 3, not including 3

#How to change values in a list
friends[1] = "Mike"
print(friends[1])
