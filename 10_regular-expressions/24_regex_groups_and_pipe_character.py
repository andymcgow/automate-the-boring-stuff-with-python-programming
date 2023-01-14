import re

# Regex objects have groups that can define different parts of an expression, such as the area code in a phone number.
# These are defined with parenthesis in the Regex object: -
phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_num_regex.search("My number is 415-555-4242")
print(mo.group())
# You can then call a specific Regex group when using the .group() command: -
print(mo.group(1))
print(mo.group(2))


# | is called the Pipe Character.
bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = bat_regex.search("Batmobile lost a wheel")
print(mo.group())
# You can also define which pipe to be seached and returned: -
print(mo.group(1))

# NOTE - if you're string DOESN'T contain any matching values then .group() will return NONE.
# It will error out as NONE doesn't have a group attribute associated with it.