# Change item value : refer index.

fruits = ["mango","apple","banana"]
fruits[1] = "grapes"
print(fruits)

# Change a range of item values.
lang = ["html" , "css" , "js" , "Ts"] 
lang[0:3] = ["react" , "python" , "sql"]
# lang[0:3] = ["react"]
print(lang)

# insert(index,value) - inserts item at specific value.
lang.insert(4,"rust")
print(lang)

# reverse() - 	Reverses the order of the list
fruits.reverse()
print(fruits)