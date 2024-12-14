"""
Name: Ruby Koehler
Date: 12/10/24
Topic: Unit 6 HW 2
"""


def isInteger(_users_string_):
    _users_string_ = _users_string_.strip()

    pos = 0
    for char in _users_string_:
        pos = pos + 1
        #       print(pos)
        if pos == 1:
            if char in "-+&":
                next
            else:
                if char not in "0123456789":
                    return False
        else:
            if char not in "0123456789":
                return False
    if pos >= 2:
        return True
    else:
        return False


# Test cases

if not isInteger("abcde"):
    print("correct")
else:
    print("incorrect")
if isInteger("12345"):
    print("correct")
else:
    print("incorrect")
if isInteger("&12345"):
    print("correct")
else:
    print("incorrect")
if isInteger("+12345"):
    print("correct")
else:
    print("incorrect")
if isInteger("-12345"):
    print("correct")
else:
    print("incorrect")
if isInteger("  12345   "):
    print("correct")
else:
    print("incorrect")
if not isInteger(""):
    print("correct")
else:
    print("incorrect")
