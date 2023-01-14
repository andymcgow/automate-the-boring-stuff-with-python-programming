my_cat = {"size": "fat", "colour": "grey", "disposition": "loud"}

print(my_cat["size"])
print("My cat has " + my_cat["colour"] + " fur.")


# Dictionaries can use intergers as keys!
spam = {12345: "Luggage combination", 42: "The Answer"}


# Dicitionaries are unordered! Example: -
# In a list, order matters. 2 lists with with the same values stored in a different order are not the same.
# But 2 dictionaries with the same key-value pairs stored in different order are.

print([1, 2, 3] == [3, 2, 1])

eggs = {"name": "Zophie", "species": "cat", "age": 8}
ham = {"species": "cat", "name": "Zophie", "age": 8}
print(eggs == ham)

print("name" in eggs)
print("name" not in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

print("cat" in eggs.values())


# You can perform lookups in dictionaries, however if that key or value doesnt exist you will get an error: -
# print(eggs["colour"]) - Will crash program as "colour" doesn't exist in eggs
# Instead you can perform an if statement: -
if "colour" in eggs:
    print(eggs["colour"])
# However this code be tedious and won't return anything if it doesn't exist.
# Instead the .get() keyword can be used, with a condition seperated by a comma to return a value if lookup doesn't exist: -
print(eggs.get("age", 0))

print(eggs.get("colour", ""))

picnic_items = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnic_items.get("napkins", 0)) + " to the picnic.")

# setdefault() can be used to set a key-value pair if one doesn't exist.
# setdefault() will only work if that key-value pair DOESN'T exist.
# 1st example using if (longer code)
if "colour" not in eggs:
    eggs["colour"] = "black"
print(eggs)
# 2nd example using setdefault()
eggs = {"name": "Zophie", "species": "cat", "age": 8}
eggs.setdefault("colour", "black")
print(eggs)
