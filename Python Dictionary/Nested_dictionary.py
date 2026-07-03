student_marks = {
    "Sagar" : {
        "maths" : 90,
        "Hindi" : 99
    }
}

# Accessing items in dictionary:
print(student_marks["Sagar"]["maths"])

# loop through nested dictionary:
for x,y in student_marks.items():
    print(x)

    for a in y:
        print(f"{a} : {y[a]}")