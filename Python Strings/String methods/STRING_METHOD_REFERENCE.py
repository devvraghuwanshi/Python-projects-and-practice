"""
Python String Methods Examples
Each example shows how a string method works.
"""

s = "hello world"
s2 = "  python  "

# upper() → converts string to uppercase
print(s.upper())

# lower() → converts string to lowercase
print("HELLO".lower())

# title() → first letter of each word capital
print(s.title())

# capitalize() → first letter capital only
print(s.capitalize())

# swapcase() → swaps uppercase to lowercase and vice versa
print("HeLLo".swapcase())

# strip() → removes spaces from both sides
print(s2.strip())

# lstrip() → removes spaces from left side
print(s2.lstrip())

# rstrip() → removes spaces from right side
print(s2.rstrip())

# replace() → replaces a substring
print(s.replace("world", "python"))

# split() → splits string into list
print(s.split(" "))

# join() → joins list elements into string
words = ["I", "love", "python"]
print(" ".join(words))

# find() → returns index of first occurrence
print(s.find("world"))

# index() → returns index (error if not found)
print(s.index("world"))

# count() → counts occurrences
print("banana".count("a"))

# startswith() → checks starting substring
print(s.startswith("hello"))

# endswith() → checks ending substring
print(s.endswith("world"))

# isalpha() → checks if all characters are letters
print("Python".isalpha())

# isdigit() → checks if all characters are digits
print("12345".isdigit())

# isalnum() → checks if letters or numbers
print("Python123".isalnum())

# isspace() → checks if only spaces
print("   ".isspace())

# islower() → checks if lowercase
print("hello".islower())

# isupper() → checks if uppercase
print("HELLO".isupper())

# istitle() → checks title case
print("Hello World".istitle())

# center() → centers string with padding
print("Python".center(20, "-"))

# ljust() → left justify
print("Python".ljust(10, "*"))

# rjust() → right justify
print("Python".rjust(10, "*"))

# zfill() → fills with zeros on left
print("42".zfill(5))