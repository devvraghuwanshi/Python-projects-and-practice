# A file is data stored in a storage device . A python program can talk to the file by reading content from it and writing content to it.

# open("filename","Mode") - 

# Modes -
# 1) Read -> "r" -> default value, opens a file for reading , error if file does not exist
# 2) Append -> "a" -> opens a file for appending , creates file if doesn't exist
# 3) Write -> "w" -> opens a file for writing , creates file if doesn't exist
# 4) Create -> "x" -> creates the specified file , returns an error if file exist
 

# we can also specify if the file should be handled as binary or text mode
# 1)"t" - text - text mode
# 2)"b" - binary - binary mode(ex, img)

# Example

f = open("Python File handling/Open files/demofile1.txt","rt")          #same as open("demofile.txt") as "rt" are default values
