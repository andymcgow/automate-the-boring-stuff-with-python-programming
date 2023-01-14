# Escape Characters \ let you put characters into strings that would otherwise be impossible or read as code: -
print('Say hi to Bob\'s mother.')
print('Hello there!\nHow are you?\nI\'m fine.')

# Raw Strings r" " allow you to use backslash characters \\\ in strings instead of interpreting them as Escape Characters: -
print(r'That is Carol\'s cat.')

# Multiline Strings in Python begin and end with triple double or single quotes (really useful for long strings): -
print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerley,
Bob.""")