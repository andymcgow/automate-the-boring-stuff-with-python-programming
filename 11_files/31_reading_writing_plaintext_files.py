# To open a plain text file you need will pass the open() command and store this in a variable: -
hello_file = open("./hello.txt")

# .read() will return a string of the files contents.
# NOTE a file can only be .read() once (without calling open() again), so the ouput will need to be stored in a varaible.
content = hello_file.read()
print(content)

# .readlines() will return a list of strings (as oppose to .read() that will return a single string).

# .close() will close a file and unload it.

# You can't write to a file opened by default, so you will have to open it in WRITE mode passing the "w" argument to open() : -
# NOTE this will OVERWRITE the existing file and replace it with a blank/empty file.
# hello_file = open("./hello.txt", "w")

# Instead of overwriting a file, you can open in APPEND mode by passing the "a" argument to open() : -
# NOTE this will allow you to ADD to the file instead of overwriting it.
# hello_file = open("./hello.txt", "a")

# NOTE that when trying to open a file using both the WRITE and APPPEND modes, if a file doesn't exist it will be created.

# write() is used to write to a file.
# write() doesn't add new lines each time it is called like print() does so you will need to specify line breaks \n if required.


# NOTE If you want to store more complex variables like dictionaires, etc you can store it in to a SHELF file.
import shelve
shelf_file = shelve.open("shelf")
shelf_file["cats"] = ["Zophie", "Pooka", "Simon", "Fat-tail", "Cleo"]
shelf_file.close()

shelf_file = shelve.open("shelf")
print(shelf_file["cats"])
shelf_file.close()

# SHELF files are similar to dictionaries and support some similar commands such as .keys() and .values() : -
shelf_file = shelve.open("shelf")
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
