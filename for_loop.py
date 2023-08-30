

for letter in "Giraffe Academy":
    print(letter)

print("-------------")

friends = ["Jim", "Karen", "Kevin"]
for friend in friends: #notice that it's friend not friends
    print(friend)

print("-------------")

friends = ["Jim", "Karen", "Kevin"]
for name in friends: #you can use any name for the elements in the array
    print(name)

print("-------------")

friends = ["Jim", "Karen", "Kevin"]
for index in range(10): #starts at 0 and doesn't include 10
    print(index)

print("-------------")

friends = ["Jim", "Karen", "Kevin"]
for index in range(3, 10): #starts at 3 and doesn't include 10
    print(index)

print("-------------")

#len(friends) == the length of the array
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index]) #this prints out each element in the array as itterate through each index

print("-------------")

for index in range(5): #starts at 3 and doesn't include 10
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")
