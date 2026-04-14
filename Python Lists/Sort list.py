# .sort() - sorts list alphanumerically , ascending order by default
# For Desending sort - .sort(reverse = True)
# sort() is a case sensitive method , all capital letters being sorted before lower case

this_list = [10,20,50,60,30,40,80,70,90,100]

this_list.sort()  #asending
print(this_list)

this_list.sort(reverse=True)
print(this_list)  #desending

fruits = ["apple","Banana","Mango","Papaya","grapes","cherrry"]
fruits.sort()
print(fruits)