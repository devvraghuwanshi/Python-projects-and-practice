# Important Python Magic / Dunder Methods


class Student:

    # 1. __init__() -> initializes object
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # 2. __str__() -> controls print(object)
    def __str__(self):
        return f"{self.name} - {self.marks} marks"

    # 3. __repr__() -> developer-friendly representation
    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    # 4. __len__() -> controls len(object)
    def __len__(self):
        return len(self.marks)

    # 5. __eq__() -> controls ==
    def __eq__(self, other):
        return self.marks == other.marks

    # 6. __lt__() -> controls <
    def __lt__(self, other):
        return self.marks < other.marks

    # 7. __add__() -> controls +
    def __add__(self, other):
        return self.marks + other.marks

    # 8. __getitem__() -> controls object[index]
    def __getitem__(self, index):
        return self.marks[index]

    # 9. __contains__() -> controls "in"
    def __contains__(self, value):
        return value in self.marks

    # 10. __call__() -> makes object callable like a function
    def __call__(self):
        print(f"{self.name} object was called")


# Creating objects
s1 = Student("Dev", [80, 85, 90])
s2 = Student("Rahul", [70, 75, 80])


# __str__()
print(s1)

# __repr__()
print(repr(s1))

# __len__()
print(len(s1))

# __eq__()
print(s1 == s2)

# __lt__()
print(s1 < s2)

# __add__()
print(s1 + s2)

# __getitem__()
print(s1[0])

# __contains__()
print(90 in s1)

# __call__()
s1()