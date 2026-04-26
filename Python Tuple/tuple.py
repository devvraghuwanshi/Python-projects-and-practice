# Tuple : tuple is a collection which is ordered , immutable , indexed , and allows duplicate values.
# index -> 0,1,2,3,........,-2,-1

# Creating tuples:

# Basic tuple:
basic_t = (1,2,3,4,5)
print(basic_t)

# packing: without parenthesis
packing = 1,2,3,4
print(packing)
print(type(packing)) # < class 'tuple'>

# single element tuple
single_el_t = ("Dev",) #comma is mandatory
print(single_el_t)

# using constructor:
constrr = tuple((1,2,"Dev",22.5,True,None)) #tuple items can be of any datatype
print(constrr)

# tuple length - len(tuple_name)
print(len(basic_t))



