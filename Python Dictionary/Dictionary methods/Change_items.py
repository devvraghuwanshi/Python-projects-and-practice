student_marks = {
    "Dev" : 100,
    "Raj" : 60,
    "Sagar" : 100
}

# using key values -
student_marks["Dev"] = 99
print(student_marks)

# update({key : new value}) or update({new key : new value})
student_marks.update({"Dev" : 98, "Nishant" : 20})
print(student_marks)