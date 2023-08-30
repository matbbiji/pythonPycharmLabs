print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("-----------------\n")

phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool") # this is concatenation
print()

print("       Functions:\n-----------------------")
'''functions are used to modify our strings and get information abt our strings'''
print("Lowercase: " + phrase.lower()) #entirely in lower case
print("Uppercase: " + phrase.upper()) #entirely in upper case

print("Is it uppercase?: ")
print(phrase.isupper()) #outputs true if phrase is uppercase

print("Making it ALWAYS uppercase")
print(phrase.upper().isupper()) #makes phrase uppercase then tells you True bc its uppercase

print("Length of " + phrase + ": ")
print(len(phrase)) #length function: tells you how many char inside string

print(phrase[0]) #outputs the character at index 0 of phrase
print(phrase.index("G")) #index function: outputs where a specific char or string is located inside of our string
print(phrase.index("Acad")) #inputing phrases gives you the index it starts at

print(phrase.replace("Giraffe", "Elephant")) #replace function: give two parameters. first is old, second is new

'''parameter: value you input inside the function'''


