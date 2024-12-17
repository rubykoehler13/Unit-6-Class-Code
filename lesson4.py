"""
Name: Ruby Koehler
Date: 12/16/24
Lesson: Tuples
"""

# Tuples are a heterogeneous (mixed types), immutable data structure
# Example of a tuple:
my_tuple = ("3", 4) #----> 2 types, thus heterogeneous
print(my_tuple)
# my_tuple[0] = 3 ----> immutable

# Make tuple with two items
my_tuple = ("3", 4)
print(my_tuple)
# Make tuple with one item
lonely_tuple = (5, ) # You have to have both () and the ,
print(lonely_tuple)

# You access elements from them using [] just like strings
print(my_tuple[0])

# Also like strings, you can only concatenate tuples with other tuples
not_lonely_tuple = my_tuple + (5,) # Doesn't work unless you do (5, )
print(not_lonely_tuple)

integer_tuple = (int(my_tuple[0]),4,5)
print(integer_tuple)

character_info = (("Rosalie", 100), ("Cedric", 75), ("Shana", 94))
print(character_info[1][0]) # Returns 'Cedric'