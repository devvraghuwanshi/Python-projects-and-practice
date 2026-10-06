# Different ways to pass arguments -

def greet(fname,lname):
    print(f"Hello , {fname} {lname}")


# 1) Keyword Arguments :
greet(fname="Dev",lname="Raghuwanshi")

# 2) positional arguments :
greet("Dev","Raghuwanshi")

# 3) Mixed :
greet("Dev" , lname="Raghuwanshi")


# Positional-only and Keyword-only :


def greet2(name,/):      #Positional only
    print(f"Hello {name}")

greet2("Dev")

def greet3(*,name):      #Keyword only   
    print(f"Hello {name}")

greet3(name="Dev")

def mixed(a,b,/,*,c,d):
    print(f"positional are {a,b} and keyword are {c,d}")

mixed(1,2,c=3,d=4)