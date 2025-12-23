s1={1,2,3,4,"ram"}
s2={1,2,5,6,"ram","krishna"}

#set.add(element), adds element to set
s1.add(55)
print(s1)

#set.remove(element), removes element from set
s1.remove(55)
print(s1)

#set.pop(), removes a random value
s1.pop()
print(s1)

#set1name.union(set2name), combines ALL elements of both sets and returns new
s3 = s1.union(s2)
print(s3)

#set1name.intersection(set2name), combines COMMON elements of both sets and returns new
s4= s1.intersection(s2)
print(s4)
