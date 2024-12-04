'''
Name: Ruby Koehler
Date: 12/4/24
Topic: Immutability, for loops, in keyword
'''

# Immutability - a string cannot be mutated or changed using [ };
# you must replace it completely

cat_name = "Franklin"
cat_name = cat_name[0:5] + "ie"
print(cat_name)

print()

###############################################################################
# For loops and strings

# You can go character by character through a string. This is called
# traversing a string

# Non-Pythonic way
cat_name = "Winston"
for i in range(len(cat_name)):
    print(cat_name[i])
print()
for i in range(len(cat_name)):
    print(cat_name[i])
    if cat_name[i] == "n":
        break

print()

# The in keyword
vowels = "aeiou"
print("a" in vowels) # prints a boolean statement
print("b" in vowels)

print()

for i in range(len(cat_name)):
    if cat_name[i] in vowels:
        print(cat_name[i])

print()

print("win" in cat_name) # comes out False b/c 'w' is not capitalized unlike in the cat's name

print()

# Use #2 - Pythonic traversal
cat_name = "Millie"
for letter in cat_name:
    print(letter, end = " ")

print()

large_number = "234450983452345"
for digit in large_number:
    print(digit, end = " ")

print("\n-------")
print(str(123) in str(12345))