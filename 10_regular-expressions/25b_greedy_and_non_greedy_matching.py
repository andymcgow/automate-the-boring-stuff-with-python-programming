import re

# By default Regular Expression searches start as soon as possible from the first matching character.
# They also try to match the largest possible string that matches a defined pattern as they look for GRADIENT matches.
# This means the below code will return "12345" when "123" or "1234" or even "67890"...
# ... matches what has been defined (if ignoring the above info).
# This is called a GREEDY match.
digit_regex = re.compile(r"(\d){3,5}")
mo = digit_regex.search("1234567890")
print(mo.group())

# You can perform a NON-GREEDY match, which will look for the smallest possible string.
# To do this, use the ? character AFTER the curly braces, such as {x, y}? : -
digit_regex = re.compile(r"(\d){3,5}?")
mo = digit_regex.search("1234567890")
print(mo.group())