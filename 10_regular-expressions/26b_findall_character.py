import re

phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

message = ("My home number is 508-555-5555 and my office number is 508-555-1234.")

# Unlike search(), the findall() doesn't return a Match Object, but instead just returns a list with all matching strings inside.
# So you don't need to store the call in a variable and then print variable.group() and instead can just print findall(): -
print(phone_regex.findall(message))

# NOTE that if there is only 1 or NO groups defined in the Regex Object, the returned list will be as above, just a list of strings.
# If 2 or MORE groups are defined in the Regex Object then the list returned by findall() with be a list of tuples, split by group: -
phone_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
print(phone_regex.findall(message))

phone_regex = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")
print(phone_regex.findall(message))