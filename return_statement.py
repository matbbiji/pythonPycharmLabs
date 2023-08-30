"""Sometimes when we call a function we're actually going to want to
get information back from that function. Execute all the code and then give
back info/communicate back with us"""

def cube(num):
    return num*num*num
    print("code") #this will never print out becasue it's after the break out code (the return statement)

result = cube(4)
print(result)
