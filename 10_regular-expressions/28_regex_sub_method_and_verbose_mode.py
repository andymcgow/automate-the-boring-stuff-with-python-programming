import re


names_regex = re.compile(r"Agent \w+")
print(names_regex.findall("Agent Alice gave the secret documents to Agent Bob."))

# sub() is a Find & Replace that uses Regex strings for the operation.
# After calling sub(), the replacement string can be added. Make sure to do this BEFORE you pass through the string.
# I.E. .sub("REPLACEMENT TEXT", "String to perform the operation on.")
print(names_regex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob."))

# The /number syntax: - /1 /2 /3 etc, uses groups in the original Regex as part of the sub() function.
# What group to use is defined by the number after the backslash, so \1 is the first group and \2 the second, and so on.
# I.E. in the below code where /sub() has been called, group \1 from the original Regex is being used as part of the subbed text.
names_regex = re.compile(r"Agent (\w)\w*")
print(names_regex.findall("Agent Alice gave the secret documents to Agent Bob."))
print(names_regex.sub(r"Agent \1*****", "Agent Alice gave the secret documents to Agent Bob."))


# VERBOSE MODE allows you to use a triple quote """ to spread out your Regex definition across multiple lines.
# This allows us to add comments in and makes it overall much easier to read and understand.
# New lines are ignored by the search, as are the # Comments. NOTE REMEMBER to use triple quotes!
# Call VERBOSE MODE when using re.compile() by adding the re.VERBOSE argument, such as re.compile(r"""\xyz""", re.VERBOSE) : -
re.compile(r"""
\d\d\d      # Area Code (without parenthesis)
-           # First Dash
\d\d\d      # First 3 digits
-           # Second Dash
\d\d\d\d    # Last 4 digits
""", re.VERBOSE)


# Only 1 value can be passed to re.compile(), so if you want to use multiple arguments you need to use the | bitwise operator: -
# The bitwise | character isn't used many other places in Python and is different from the | pipe character used in Regex definitions.
# It is a hangover from older programming languages that isn't really used much anymore.
re.compile(r"""\d\d\d""", re.I | re.DOTALL | re.VERBOSE)