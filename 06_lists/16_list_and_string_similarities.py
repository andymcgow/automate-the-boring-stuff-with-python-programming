# Strings are immutable values and CANNOT be modified in place.
# When you assign a variable containing a string to a new variable
# The string is copied to the new variable and is separate from the original variable.

# Lists are mutable values and CAN be modified in place.
# When you assign a varaible containing a list to a new variable,
# the original list is only referenced by the new variable as is linked.
# Any changes to the new variable will also change the list in the original variable.

spam = ["A", "B", "C", "D"]
cheese = spam
cheese[1] = 42
print(cheese)
print(spam)


# Using .deepcopy allows you to completely copy (NOT reference) a mutable value to a new variable.

import copy

spam = ["A", "B", "C", "D"]
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)