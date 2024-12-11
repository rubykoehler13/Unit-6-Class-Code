"""
Name: Ruby Koehler
Date: 12/10/24
Topic: Unit 6 HW 2
"""
while True:
    def isinteger(user_string):
        user_string = user_string.strip()

        pos = 0
        for char in user_string:
            pos = pos + 1
            print(pos)
            if pos == 1:
                if char in "-+&":
                    continue
                else:
                    if char not in "0123456789":
                        print("False")
                        break
            else:
                if char not in "0123456789":
                    print("False")
                    break
        if pos >= 2:
            print("True")
                    break
        else:
            print("False")
                    break

# Test Cases:
    isinteger("abcde")
    isinteger("12345")
    isinteger("&12345")
    isinteger("+12345")
    isinteger("-12345")
    isinteger("     12345     ")
    isinteger("")