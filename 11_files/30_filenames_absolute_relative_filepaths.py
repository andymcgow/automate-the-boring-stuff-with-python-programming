import os

# os.path.join() takes a file path, saved as a string, seperated by commas and joins it together correctly for the host OS.
# I.E. os.path.join("folder 1", "folder 2", "folder 3", "file.ext")

# os.cdw() gets the current working directory.

# os.chdir() changes the directory to a specified location.

# . refers to the current folder

# .. refers to the parent folder (one level up)

# os.path.abspath() will return/convert an absolute path for a given relative path.

# os.path.isabs() will check if a path is absolute and return True or False.

# os.path.relpath() will return/convert a relative path from a starting path to another.
# I.E. os.path.relpath("DESTINATION PATH", "STARTING PATH")

# os.path.dirname() will return an directory path to a file NOT including the file.

# os.path.basename() will return a filename from a path WITHOUT the directory path itself.
# (It will also return the last folder in the path if no file is specificed.)

# os.path.exists() checks if a path exists.

# os.path.isfile() checks if a path ends in a file.

# os.path.isdir() checks if a path ends in a directory.

# os.path.getsize() checks the size of a file. (or directory?)

# os.listdir() will return a list of strings with all the folders and files inside a path.

# Example code for checking the total size of all files in a directory: -
# total_size = 0
# for filenamein os.listdir("PATH HERE"):
#     if not os.path.isfile(os.path.join("PATH HERE", filename)):
#         continue
#     total_size = total_size + os.path.getsize(os.path.join("PATH HERE", filename))

# os.makedirs will make a directory.
