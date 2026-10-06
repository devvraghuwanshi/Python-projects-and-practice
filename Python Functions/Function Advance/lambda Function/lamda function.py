# Lambda function : function written in one line using lambda keyword , accepts any number of arguments , but only one expression
# Usefull if needed for short period of time , throw-away

# SYNTAX : lambda  parameter : expression

# Examples:
double = lambda x : x * 2
multiply = lambda x,y : x * y
add = lambda x,y,z : x + y + z
full_name = lambda first_name , last_name : f"{first_name} {last_name}"
check_age = lambda age : True if age >= 18 else False

print(double(2))
print(multiply(2,2))
print(add(2,2,2))
print(full_name("Dev","Raghuwanshi"))
print(check_age(17))