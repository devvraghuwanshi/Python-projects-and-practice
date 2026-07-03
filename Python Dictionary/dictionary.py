# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered , mutable , indexed and do not allow duplicates.

# Declaring dict -
student_marks = {
    "Dev" : 100,
    "Raj" : 60,
    "Sagar" : 100
}
print(type(student_marks))
print(student_marks)
print(len(student_marks)) #Gives length of Dictionary

# Declaring dict using constructor -
marks = dict(dev = 100,raj = 70 , sagar = 100)
print(marks)
