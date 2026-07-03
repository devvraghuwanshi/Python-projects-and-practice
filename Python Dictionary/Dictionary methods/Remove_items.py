student_marks = {
    "Dev" : 100,
    "Raj" : 60,
    "Sagar" : 100,
    "nishant" : 20
}

# pop(key) - remove item with specified key name.
student_marks.pop("Dev")
print(student_marks)

# popitem() - removes last  item
student_marks.popitem()
print(student_marks)

# del keyword - 
del student_marks["Raj"] #removes item with specified key name
del student_marks        #deletes dict completely

marks = {
     "Dev" : 100,
    "Raj" : 60,
    "Sagar" : 100,
    "nishant" : 20
}
# clear() - empties dictionary , dictionary remains but becomes empty
print(marks.clear())