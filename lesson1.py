'''
Name: Ruby Koehler
Date: 12/2/24
Topics: Indexing, Slicing, Immutability
'''

# Review
name = "Starla" # a string literal

# f-strings (formatted strings)
description = f"{name} likes wand toys"

print(description)

#same result with concatenation
age = 5
description = name + " likes wand toys and is " + str(age)
print(description)

# indexing - every character in a string has a location
# starting at 0, ex:
#  S  t  a  r  l  a
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

first_letter = name[0] # always use 0 if you don't know length
print(first_letter)
first_letter = name[-6]
print(first_letter)
first_letter = name[-1*len(name)]
print(first_letter)

last_letter = name[-1] #always use if you don't now length
print(last_letter)
last_letter = name[len(name)-1]
print(last_letter)

# use [ ] to access a character - not (), it gives TypeError
# accessing an index that does not exist gives IndexError

try:
    print(name[20])
except IndexError:
    print("Out of bounds")

# HW for Lesson 1 is 7.1.5 and 7.1.6
#######################################################################################################################
# Slicing - used to access 1 or more characters in a string
# Instead of name[0] + name[1] + name[2], etc., we can do name[0:3]

# first three letters
first_three = name[0] + name[1] + name[2]
print(first_three)
first_three = name[0:3] #start at index 0, go up to but not including index 3
print(first_three)

# Format:
# string_name[start:stop:step] - non are technically required

word_one = "Adventure"

# What is the result of print(word_one[3:]) - leaving out stop
print(word_one[3:])
# Try leaving out start
print(word_one[:3])
# Try leaving out both!
print(word_one[:])
# Try negative indices?
print(word_one[:-3])
print(word_one[-3:])
# Try nothing but a negative step
print(word_one[::-1])
print(word_one[-3:-7:-2])
print(word_one[-7:-3:-2])

# HW for Lesson 2 is 7.2.6 - 7.2.8