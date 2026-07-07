# to delete file , import OS and use os.remove() function

import os

# os.remove("Python File handling/Delete files/delete_this_file.txt")

# check if file exists to avoid error
if os.path.exists("Python File handling/Delete files/delete_this_file.txt"):
    os.remove("Python File handling/Delete files/delete_this_file.txt")
else:
    print("file does not exists")
