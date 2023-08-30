
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #special line of code in python to check letters
            if letter.isupper():
                translation = translation + "G"
            else:
                translation + translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))