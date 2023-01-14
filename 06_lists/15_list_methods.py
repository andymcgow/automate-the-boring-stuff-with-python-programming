# index()

# spam = ["hello", "hi", "howdy", "heyas"]
# print(spam.index("hello"))
# print(spam.index("heyas"))
# print(spam.index("fwefwelfhweiofjweif")) # Will return an error this is not in the list

# spam = ["Zophie", "Pooka", "Fat-tail", "Pooka"]
# spam.index("Pooka") # If there is a duplicate value in the list, only the first index will be returned


# append()

# spam = ["cat", "dog", "bat"]
# spam.append("moose")
# print(spam)


# insert()

# spam = ["cat", "dog", "bat"]
# spam.insert(1, "chicken")
# print(spam)


# remove() - Note, only the FIRST instance of a value will be removed
# remove() works differently to del spam[0] as it uses a VALUE and not an INDEX

# spam = ["cat", "bat", "rat", "elephant"]
# spam.remove("bat")
# print(spam)


# sort() - Works for both numbers and strings, uses 'ASCI-betical' order (Upper-case comes before lower-case)

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

# Example of ASCI-betical sorting
spam = ["Alice", "Bob", "ants", "badgers", "Carol", "cats"]
spam.sort()
print(spam)

# Get true alphabetical sorting with keyword key=str.lower
spam = ["a", "z", "A", "Z"]
spam.sort(key=str.lower)
print(spam)
