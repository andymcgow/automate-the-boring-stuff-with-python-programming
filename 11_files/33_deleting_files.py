import os
# os.unlink() can delete single files: -
os.unlink("filename.xyz")

# os.rmdir() can delete folders: -
# NOTE os,rmdir() can only delete folders if they are completely EMPTY.
os.rmdir("path/to/empty/folder")


import shutil
# shutil.rmtree() WILL delete a folder that has contents: -
shutil.rmtree("path/to/folder")

# NOTE - Extra caution should be taken with these commands, especailly os.unlink() and shutil.rmtree() !
# These commands DO NOT move files to the BIN - they are instantly and permenantly DELETED.

# One way to work around this do to a 'Dry Run': -
# Comment out # any code that WOULD perform a deletion and instead use print() to display what would be deleted.
# Check the output of the print() command to ensure it is as expected before uncommenting the DELETE code.
for filename in os.listdir():
    if filename.endswith(".xyz"):
        # os.unlink("filename")
        print("filename")


# A safer way to delete files is to use the SEND2TRASH module: -
# send2trash doesn't come with Python so will need to be installed via pip.
import send2trash
send2trash.send2trash("path/to/file.xyz")
