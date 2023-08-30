
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(number_grid[2][1]) == this is how you print out a specific element in the 2d list


'''Parsing through a normal grid/2d list. You have to use 2 for loops'''

for row in number_grid: #we used row in the ex because each index is like a row
    for col in row: #NOTICE we're parsing through row
        print(col)