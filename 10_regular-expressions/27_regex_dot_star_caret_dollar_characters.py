import re


# You can use the ^ symbol to state the Regex character class MUST be found at the START of a searched string: -
# NOTE this is different to the ^ symbol's usage in CUSTOM character classes.
begins_with_hello_regex = re.compile(r"^Hello")
print(begins_with_hello_regex.search("Hello there!"))
print(begins_with_hello_regex.search("He said Hello!"))

# Conversely, the $ dollar sign can be used to state that the Regex character class MUST be found at the END of a searched string: -
ends_with_world_regex = re.compile(r"world!$")
print(ends_with_world_regex.search("Hello world!"))
print(ends_with_world_regex.search("Hello world, hello!"))

# You can combine the ^ and $ methods together to state that a searched string MUST START and END with the Regex character class: -
all_digits_regex = re.compile(r"^\d+$")
print(all_digits_regex.search("1234567890"))
print(all_digits_regex.search("12345x67890"))


# The . period symbol is the WILDCARD character stands for ANY character EXCEPT a new line: -
at_regex = re.compile(r".at")
print(at_regex.findall("The cat in the hat sat on the flat mat."))

# Notice above that 'flat' isn't matched and instead 'lat' is returned.
# This is because the Regex character class is only looking for 1 extra digit.
# We can modify the above Regex character class to search for 1 or 2 or any other character, but note how spaces are also returned: -
# (It REALLY does mean ANY character bar a new line character!)
at_regex = re.compile(r".{1,2}at")
print(at_regex.findall("The cat in the hat sat on the flat mat."))

# Instead, to get around this problem, .* (dot-star) matching is commonly used.
# .* essentially means ANY OR MORE so will match a wider scope of patterns.
name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
print(name_regex.findall("First Name: Al Last Name: Sweigart"))

# NOTE .* is GREEDY
# To make it NON-GREEDY use the ? symbol, such as (.*?) : - 
serve = "<To serve humans> for dinner.>"
# NON-GREEDY example: -
non_greedy_regex = re.compile(r"<(.*?)>")
print(non_greedy_regex.findall(serve))
# GREEDY example (no ? symbol): -
greedy_regex = re.compile(r"<(.*)>")
print(greedy_regex.findall(serve))


# NOTE how the . period symbol really will find every, but is stopped by a \n new line character: - 
prime = "Serve the public trust.\nProtect the innocent.\nUphold the law."
dot_star_regex = re.compile(r".*")
print(dot_star_regex.search(prime))
# By passing the re.DOTALL argument you can make the . period symbol apply to everything INCLUDING \n new line characters.
dot_star_regex = re.compile(r".*", re.DOTALL)
print(dot_star_regex.search(prime))


# To ignore case sensitivity, you can pass the argument re.IGNORECASE, or in a shorter for re.I : -
vowel_regex = re.compile(r"[aeiou]", re.I)
print(vowel_regex.findall("Al, why does your programming book talk about RoboCop so much?"))
