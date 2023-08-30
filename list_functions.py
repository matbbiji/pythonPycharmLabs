
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers) #extend function: take one list, and append an entire list to it
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed") #append function: adding an element at the end into an already existing list
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly") #insert function: insert an element anywhere in the list. requires 2 parameters: index to place new element, the element
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim") #remove function: removes one specified element from the list
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear() #clear function: empties out the entire list
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop() #pop function: removes last element of the list
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#index function: use this method to find where a specific element exists in the list
print(friends.index("Kevin"))

"""COUNTING SIMILAR ELEMENTS"""
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] #NOTICE I changed the list
#count function: returns the number of times the parameter shows up in the list
print(friends.count("Jim"))

"""SORTING LISTS"""
lucky_numbers = [42, 8, 15, 16, 23, 4] #changed this too
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] #NOTICE I changed the list
friends.sort()#sort function: sorts the list in either alphabetical or ascending order
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

"""REVERSE SORTING LISTS"""
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] #NOTICE I changed the list
lucky_numbers.reverse()
print(lucky_numbers)

"""CREATING ANOTHER LIST/A COPY"""
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] #NOTICE I changed the list

friends2 = friends.copy()

print(friends2)
