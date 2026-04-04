# SYNTAX:
# if condition:
#    #code to execute if condition is True

# WORKING:The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.


# EXAMPLE:
number = 15
if number > 0:
    print("Number is positive")


# Multiple statements in if block:
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


# Using variable in conditions:
is_logged_in = True
if is_logged_in:
   print("User is logged in")


# Shorthand if: only use when you have only one statement
# SYNTAX : if condition : code to execute
a=5
b=3
if a>b : print("a is greater than b")