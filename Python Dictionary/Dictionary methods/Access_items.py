student_marks = {
    "Dev" : 100,
    "Raj" : 60,
    "Sagar" : 100
}

# using key name - 
print(student_marks["Dev"])  #Gives error when key is not present

# get(key) - gives key value (prints none when key is not present)
print(student_marks.get("Dev"))

# keys() -  returns list of all keys in dict.
print(student_marks.keys())

# values() - returns a list of all values in dict.
print(student_marks.values())

# items() - return each item in a dict.
print(student_marks.items())


# Membership - "in" keyword - checks if key is present in dict or not
if "Dev" in student_marks:
    print("Yes Dev is present")