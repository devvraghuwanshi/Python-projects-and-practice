# with statement - alternate way to open file
# no need to worry about closing the file when using with statements

with open("Python File handling/Read files/demofile2.txt") as f:
    data = f.read()
    print(data)