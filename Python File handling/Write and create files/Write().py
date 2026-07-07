# write to an existing file -

# 1) "a" - append - will append to the end of the file

with open("Python File handling/Write and create files/demofile.txt" , "a") as f:
    f.write("This is added using append")
   
#open and read the file after the appending:
with open("Python File handling/Write and create files/demofile.txt") as f:
    print(f.read())


# 2) "w" - write - will ovewrite any existing content 
with open("Python File handling/Write and create files/demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("Python File handling/Write and create files/demofile.txt") as f:
  print(f.read()) 