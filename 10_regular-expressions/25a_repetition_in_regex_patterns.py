import re

# The ? character states that a string/group defined in the Regex object can be included 0 or 1 times but not more than that, for example: -
bat_regex = re.compile(r"Bat(wo)?man")
mo = bat_regex.search("The Adventures of Batman")
print(mo.group())
mo = bat_regex.search("The Adventures of Batwoman")
print(mo.group())
# The below will error out as it returns NONE as wowowo is repeated too many times: -
# mo = bat_regex.search("The Adventures of Batwowowoman")
# print(mo.group())

phone_regex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo = phone_regex.search("My phone number is 415-555-1234. Call me tomorrow.")
print(mo.group())
mo = phone_regex.search("My phone number is 555-1234. Call me tomorrow.")
print(mo.group())


# The * character means match 0 OR more times: -
bat_regex = re.compile(r"Bat(wo)*man")
mo = bat_regex.search("The Adventures of Batman")
print(mo.group())
mo = bat_regex.search("The Adventures of Batwoman")
print(mo.group())
mo = bat_regex.search("The Adventures of Batwowowoman")
print(mo.group())


# The + character means the group MUST appear 1 or more times: -
bat_regex = re.compile(r"Bat(wo)+man")
# The below string would error out "wo" isn't in the string: -
# mo = bat_regex.search("The Adventures of Batman")
# print(mo.group())
mo = bat_regex.search("The Adventures of Batwoman")
print(mo.group())
mo = bat_regex.search("The Adventures of Batwowowoman")
print(mo.group())


# If you want to literally search for any special characters in a string that are normally reserved for Regex operations,
# Such as "+", "*" or "?", then you will need to use the \ character before them when defining the Regex object: -
regex = re.compile(r"\+\*\?")
mo = regex.search("I learned about +*? regex syntax today.")
print(mo.group())


# {x} searches the string to find an expression that matches exactly "x" times: -
ha_regex = re.compile(r"(Ha){3}")
mo = ha_regex.search("He said 'HaHaHa'")
print(mo.group())

phone_regex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}")
mo = phone_regex.search("My numbers are 415-555-1234,555-4242,212-555-0000")
print(mo.group())
# You can add a comma to the {x} function to match a range, such as {x, y} : -
ha_regex = re.compile(r"(Ha){3,}")
mo = ha_regex.search("He said 'HaHaHa'")
print(mo.group())
mo = ha_regex.search("He said 'HaHaHaHaHa'")
print(mo.group())
# You can also add a comma, but not specify an upper range to leave it unbounded to check an infinte number of repeats, such as {x,} : -
mo = ha_regex.search("He said 'HaHaHaHaHaHaHaHaHaHa'")
print(mo.group())
