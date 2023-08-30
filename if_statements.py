
is_male = True

if is_male:
    print("You are a male") #needs an indentation
else:
    print("You are not a male")

"""Checking more than one value with OR operator"""
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

'''AND operator'''
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

'''Else if operator: all conditions/combos accounted for'''
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")