t1 = (1,2,3,4,5)
print(t1)

#accessing elements of tuplethrough index
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1[4])
# print(marks[5]) : index out of range

"""
tuples are immutable, hence elements cannot be changed with index accessing
t1[0] = "10"
print(t1)
"""

#tuples slicing is same as list slicing
print(t1[1 : 4])
print(t1[0 : 3])
print(t1[0 :  ])        
print(t1[  : 4])
print(t1[-3 : -1])

#tuplename.index(element), returns index of first occurence
t2 = (10,20,30,40,50,10)
print(t2.index(10))

#tuplename.count(element), returns total occurences of element
print(t2.count(10))