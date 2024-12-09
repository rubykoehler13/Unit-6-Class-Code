'''
Name: Ruby Koehler
Date: 12/9/24
Topics: More strings
'''

# Upper case
name = "starla"
print(name.upper()) # this prints 'STARLA'
print(name) # this prints 'starla' - nothing changed

name = name.upper() # this will replace the function 'name' with STARLA
print(name) # prints 'STARLA'

# Lower case
name = "FRANKLIN"
print(name.lower()) # prints 'franklin'

# Title case
sentence = "FRANKLIN LEAVE MILLIE ALONE"
print(sentence.title()) # prints sentence with just the first letters of each word capitalized

# Swap case
word = "ViOlIn"
print(word.swapcase()) # swaps capital letters for lowercase and vice versa

# Strip
school = "           Oregon State           University           "
print(school.strip()) # only removes white space at beginning

# 'find' = returns index of first occurrence, -1 if not found

print("Oregon State University".find("go")) # prints '3' because 'go' occurs after index 3

##########################################################################

# Boolean checks
print("B".isupper()) # prints True because 'B' is uppercase
print("B".islower()) # prints False because 'B' is lowercase
print("B".isalpha()) # prints True
print("B".isalnum()) # letter or number
print("B".isdigit()) # prints False because 'B' isn't a digit (number)