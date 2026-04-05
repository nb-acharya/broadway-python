print("----DAY 5------")
print("LIST IN PYTHON")

data = ["string",23,22.22]

data[0] = "changed"

# three ways to add or remove the data -> append, insert, extends,concat
"""
append add data in the end of the list
insert  add data in any index
extends 
"""

a = [1,2,3,4,5,5]
a.append(45)
print(a)


new_list = ["beijing","hanoi"]
new_list.insert(1,"niroj")
print(new_list)


new_list.insert(100,"finding") #insert at last index, there is no index, but error doesnt show up.


print("-------extend method----------")
var1 = [3,4,5,6]
var2 = [90,100,101]

var3 = var1.extend(var2) #problem in assignment:
print(var3)

print("-----concat------------")

var1 = [3,4,5,6]
var2 = [90,100,101]

var3 = var1 + var2 #no problem in assignment
print(var3)


tot = [33,44,55]

random = tot.insert(5,"niroj")
print(random) #see how random is None, its like when list is being worked on, it cannot be assigned.

print("----------slicing------------")

data20 = [45,46,47,48,49,50]


print(data20[0:3])
print(data20[:3])
print(data20[:])

print("-------remove items from list")
# del is used to remove the variable completely and can also remove specific index from list

#remove
data21 = [1,2,2,4,5]
data21.remove(5)
print(data21)


#pop
data22 = ["gg","tt","cc"]
data22.pop()
print(data22)

# # you can't pop from empty list
# data23 = []
# data23.pop()


numbers = [1, 2, 3]
rev_numbers = numbers[::-1]
print(rev_numbers)