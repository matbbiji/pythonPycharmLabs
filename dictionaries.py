"""Dictionaries store key value pairs and to located one you use its key
ex: in an actual dictionary, the word is used to identify the definition you lookin for.
in that sense, the key is like the word. The value would be the actual definition"""

#dictionaries need the open and closed curly brackets
#keys cannot be the same. also need comma's to seperate each one
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"]) #refer to the key to output the value
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a valid Key")) #.get() is good to use when wanting a default value

#can also use numbers as the key instead of "Jan", "Feb", etc.