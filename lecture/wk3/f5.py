"""
What is a string method
    string: a text data type
        collection of characters
    method
        an action on something
    string method
        an action of the string data type
        When do we use them?
            when you want to transform, analyze text

    Syntax of using a string method
        stringDataType.method_name()
"""

name = "Johnny"
all_caps = name.upper()
print(all_caps)
all_lower = name.lower()
print(all_lower)

movie = "john wick"
proper_title = movie.title()

print("abc def cool beans!".find("def")) # 4

print("ajfdajfafdadfafadmblvmqo".capitalize())
print("Ben".swapcase())  # bEN

# testing

print("Hello there!".isupper())  # False

print("how about this?".islower())  # ???

print("12.34".isdigit())  #

print("dfjadfj2o3u98afak".isalpha())  # False

print("dfjadfj2o3u98afak".isalnum())  # True

print("I love python".center(31, "*"))