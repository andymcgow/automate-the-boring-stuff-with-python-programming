import os, shutil

# os.walk() returns a map of a specific file path, including all sub-folders and files.
# It requires naming 3 variables and can be used in FOR LOOPS: -
for folder_name, sub_folders, file_names in os.walk("file/path"):
    print("The folder is " + folder_name)
    print("The sub-folders in " + folder_name + " are: " + str(sub_folders))
    print("The filenames in " + folder_name + " are:" + str(file_names))

    for sub_folder in sub_folders:
        if "xyz" in sub_folder:
            os.rmdir(sub_folder)
    
    for file in file_names:
        if file.endswith(".xyz"):
            shutil.copy(os.join(folder_name, file), os.join(folder_name, file + " backup"))

# NOTE - REMEMBER to do a DRY RUN on any code that will be deleting, moving or copying large amounts of files.
# Comment # out potentially dangerous code and use print() to check the output first!