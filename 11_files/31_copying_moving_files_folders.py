# shutil provides the ability to copy and move files. First it needs to be imported: -
import shutil

# FILE COPY using .copy() : -
shutil.copy("path/to/file.xyz", "path/to/destination")

# You can also RENAME the file while copying by specifying a desination name: -
shutil.copy("path/to/file.xyz", "path/to/destination/new_name.xyz")

#  FOLDER COPY using .copytree() : -
# NOTE this will RENAME the copied folder if the end of the path doesn't exist.
shutil.copytree("path/to/folder", "path/to/destination")

# You can MOVE files instead of just copying with .move() : -
shutil.move("path/to/file.xyz", "path/to/destination")

# NOTE shutil doesn't have a RENAME function.
# Instead you can use .move() to 'move' a file to the same location but with a new name.
# (This has the same effect as renaming the file.)
shutil.move("path/to/file.xyz", "path/to/new_name.xyz")
