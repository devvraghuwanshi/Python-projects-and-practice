# Python comes with many built-in modules

# math module - used for mathematical functions and constants
import math

# mathematical constants:
print(math.pi)            #gives value of pi
print(math.e)             #gives value of eulers number
print(math.tau)           #tau = 2 * pi
print(math.inf)           #represents positive infinity
print(math.nan)           #reperesents not a number


# Power and Root Functions:
print(math.sqrt(16))      #sqrt(x) - returns square root of x
print(math.pow(2,4))      #pow(x,y) - raises x to the power y

# Absolute value:
print(math.fabs(-25))     #fabs(x) - returns absolute value as float

# Rounding functions:
print(math.ceil(5.3))     #ceil(x) - rounds up X
print(math.floor(5.3))    #floor(x)- rounds down X
print(math.trunc(5.333))  #trunc(x)- removes decimal part of x

# Factorial :
print(math.factorial(5))  #factorial(n)-gives factorial of n

# common factors:
print(math.gcd(10,20))    #gcd(x,y) - gives greatest common divisor of x and y
print(math.lcm(10,20))    #lcm(x,y) - gives least common multiple of x and y

# logarithmic function:
print(math.log(10))       #log(x) - gives natural log
print(math.log10(1000))   #log10(x) - base 10 log
print(math.log2(8))       #log2(x) - base 2 log

# Exponential function:
print(math.exp(2))        #exp(x) - returns e to the power x

# Trigonometric functions:python excepts angles in radians not in degree
print(math.sin(math.radians(90)))
print(math.cos(math.radians(90)))
print(math.tan(math.radians(90)))

# radian and degree conversions:
print(math.radians(180))  #math.radians(deg) - converts degree into radian
print(math.degrees(math.pi))  #math.degrees(rad) - converts radian into degree

# Distance function:
print(math.hypot(10,20))  #math.hypot(b,h) - calculates hypotenus according to pythagoras theorem

# Floating point comparision:
print(math.isclose(1.1+1.2,1.3)) #compares floating point numbers safely

# Checking numbers:
print(math.isfinite(10))   #isfinite(x) - checks if number is finite
print(math.isinf(10))      #isinf(x) - checks if x is infinite
print(math.isnan(10))      #isnan(x) - checks if x is not a number

# Summations and products:
print(math.fsum([1.2,1.3,2.5])) #fsum() - provides more accurate floating point sum
print(math.prod([1,2,3,4,5,6])) #prod() - multiply all numbers in an iterable

# Permutation and combination:
print(math.comb(5,2))      #comb(n,r) - returns number of combination
print(math.perm(5,2))      #perm(n,r) - returns number of permutation

