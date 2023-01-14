# # Example of code that checks if a string is a phone number WITHOUT using Regular Expressions: -
# def is_phone_number(text):
#     if len(text) != 12:
#         return False # Not phone number sized
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False # No area code
#     if text[3] != '-':
#         return False # Missing dash
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False # Not first 3 digits
#     if text[7] != '-':
#         return False # Missing second dash
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False # Missing last 4 digits
#     return True

# print(is_phone_number("415-555-1234"))
# print(is_phone_number("hello"))


# # Even MORE code would be needed to check a larger string such as a sentence.

# # Example containing phone numbers: -
# message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
# found_number = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if is_phone_number(chunk):
#         print("Phone number found: " + chunk)
#         found_number = True
# if not found_number:
#     print("Could not find any phone numbers.")

# # Example NOT containing phone numbers: -
# message = "Call me at 415-555 tomorrow. 555-9999 is my office."
# found_number = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if is_phone_number(chunk):
#         print("Phone number found: " + chunk)
#         found_number = True
# if not found_number:
#     print("Could not find any phone numbers.")


# Version of the above code using Regular Expressions: -
import re

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# .search() will return the FIRST matching string as defined above.
# .group() will need to be used to return the matching string.
mo = phone_num_regex.search(message)
print(mo.group())

# .findall() will return a list containing ALL the matching strings.
mo = phone_num_regex.findall(message)
print(mo)
