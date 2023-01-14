import re


# Below is the shorthand for the Regex Character Classes: -
# \d - Any numeric digit from 0 to 9.
# \D - Any character that is not a numeric digit from 0 to 9.
# \w - Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W - Any character that is not a letter, numeric digit, or the underscore character.
# \s - Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S - Any character that is not a space, tab, or newline.


lyrics = """
12 drummers drumming, 
11 pipers piping, 
10 lords a leaping, 
9 ladies dancing, 
8 maids a milking, 
7 swans a swimming, 
6 geese a laying, 
5 golden rings, 
4 calling birds, 
3 french hens, 
2 turtle doves, 
and 1 partridge in a pear tree.
"""


# The below Regex expression uses the \d (numeric digit), \s (space character) and the \w (letter character),
# combined with the + (1 or more) to find the number of with the first word from the lyrics above: -
xmas_regex = re.compile(r"\d+\s\w+")
print(xmas_regex.findall(lyrics))


# Making your own character classes can be achieved by using the square braces, such as (r"[xyz]") : -

# The below Regex character class is set to search for vowels: -
vowel_regex = re.compile(r"[aeiouAEIOU]")
print(vowel_regex.findall("Robocop eats baby food."))

# The below Regex character class is looking for a pair of vowels: -
vowel_regex = re.compile(r"[aeiouAEIOU]{2}")
print(vowel_regex.findall("Robocop eats baby food."))

# The below Regex character class is looking for a range or letters in alphabetical order: -
abc_regex = re.compile(r"[a-f]")
print(vowel_regex.findall("abcdefghijklmnopqrstuvwxyz"))


# You can use custom character classes to perform NEGATIVE character classes/searches.
# By using the ^ symbol you can turn your character class negative, such as (r"[^xyz]") : -
# So now, by using the ^ symbol on our previous vowel character class, we can make it find consonants: -
consonants_regex = re.compile(r"[^aeiouAEIOU]")
print(consonants_regex.findall("Robocop eats baby food."))