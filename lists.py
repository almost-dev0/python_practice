marks = [10,20,30,40,50]
print(marks)

#accessing elements of list through index
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5]) : index out of range

#len(listname), returns length of list
print("Number of elements in list : ",len(marks))

#we can also store heterogeneous data
details = ["Omkar",25,"Ahilyanagar"]
print(details)

#lists are mutable, hence elements can be changed with index accessing
print(details[0])
details[0] = "Vishal"
print(details)

#list slicing is same as string slicing
print(marks[1 : 4])
print(marks[0 : 3])
print(marks[0 :  ])        
print(marks[  : 4])
print(marks[-3 : -1])

#listname.append, adds one element at end,returns NONE hence we have to print list again
marks.append(70)
print(marks)

#listname.sort(), sorts in ascending order, returns NONE hence we have to print list again
#listname.sort(reverse = True), sorts in descending order, returns NONE hence we have to print list again
print(marks.sort())
print(marks)
print(marks.sort(reverse = True))
print(marks)

#sort function also applies on strings
l1 = ['a','b','c']
l1.sort()
print(l1)
l1.sort(reverse = True)
print(l1)

#listname.reverse, reverses the entire list
ranks = [1,2,3,4,5]
ranks.reverse()
print(ranks)


#listname.insert(index,element), adds element at given index
l2 = [1,3,4,5]
l2.insert(1,2)
print(l2)

#listname.remove(element), remove first occurence of elememt
l3 = [1,1,2,3,4]
l3.remove(1)
print(l3)

#listname.pop()  removes last element, pop(index) removes element at givenindex
l4 = [1,2,3,4]
l4.pop()
l4.pop(2)
print(l4)