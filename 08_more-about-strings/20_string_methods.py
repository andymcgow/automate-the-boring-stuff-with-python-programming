spam = "Hello world!"

print(spam.upper())
# Strings are immutable so the above code only prints spam in uppercase,
# spam is still stored as line 1 as it cannot be modified in-place.
# spam = spam.upper() WOULD replace spam with all uppercase letters.

print(spam.lower())

# .upper() and .lower() are great for performing expressions on user inputs,
# as you have no control as to what a user may input, i.e. Yes, yes or YES.
# This is especially useful if you need to perform if comparison statements on them,
# i.e. Instead of if answer == "yes" etc you can use if answer.lower() == "yes"

# islower() and isupper() can be used to check if a string is all upper or lower case.
print(spam.isupper())
print(spam.islower())

# isalpha() - letters only
# is alnum() - letters and number only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - titlecase only

# startswith() - checks if a string begins with a defined string or character: -
print("Hello world!".startswith("Hello"))
print("Hello world!".startswith("H"))
print("Hello world!".startswith("World"))

# endswith() - checks if a string ends with a defined string or character: -
print("Hello world!".endswith("world!"))
print("Hello world!".endswith("!"))
print("Hello world!".endswith("W"))

# .join - joins a list of strings into a single single string value: -
print(",".join(["cats", "rats", "bats"]))
print("".join(["cats", "rats", "bats"]))
print(" ".join(["cats", "rats", "bats"]))
print("\n\n".join(["cats", "rats", "bats"]))

# .split - Does the opposite to .join - it splits a string into a list of strings: -
print("My name is Simon".split())
# .split uses spaces as the default split character, but you can pass in different methods: -
# (It WILL delete the split character just like it removes spaces)
print("My name is Simon".split("m"))

# rjust() and ljust() fill a string with spaces to make it a certain length while justifying left or right: -
print("Hello".rjust(10))
print("Hello".ljust(20))
# Optional arguments can be passed to change the fill character: -
print("Hello".rjust(20, "*"))
print("Hello".ljust(25, "-"))

# center() does the same but centering the string instead of justifying left or right: -
print("Hello".center(20))
print("Hello".center(20, "="))

# strip() removes white space from strings, use lstrip or rstrip to define left or right: -
x = "     x     "
print(x.strip())
print(x.lstrip())
print(x.rstrip())
# You can also pass a string or characters to be removed, up to the first instance of a non-specificed character: -
print("SpamSpamBaconSpamEggsSpamSpam".strip("ampS"))

# replace() - Takes to arguments, first a character or string to find then a second with what to replace with: -
spam = "Hello there!"
print(spam.replace("e", "XYZ"))

# The pyperclip module has the ability to copy and paste to the clipboard which is useful for automating sending emails, etc.
# pyperclip is not installed by default with Python so WILL need installing on any system you wish to run your program.

import pyperclip
pyperclip.copy("Hello!!!!!")
print(pyperclip.paste())
