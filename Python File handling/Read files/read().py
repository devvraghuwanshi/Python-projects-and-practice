# read() - reads content of file , returns whole text


f = open("Python File handling/Read files/demofile2.txt","rt")
data = f.read()
print(data)

# close() - closes the file
# It is good practice to close the file when you are done with it
f.close()


# read(value) - this reuturns specified number of characters
f = open("Python File handling/Read files/demofile2.txt","rt")
data = f.read(5)
print(data)
f.close()

# readline() - returns one line of the text
f = open("Python File handling/Read files/demofile2.txt","rt")
print(f.readline())
print(f.readline())
f.close()

# Looping through file line by line
with open("Python File handling/Read files/demofile2.txt","rt") as f:
    for x in f:
        print(x)
