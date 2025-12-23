#set is for storing unique and immutable values

set1 = {1,2,3,4,5}
print(set1)

set2 = {1,2,2,4,3,5,4,4,1,2,5,4,3,4}
print(set1) #op is {1,2,3,4,5}, because even if we store multiple same values it only prints a single value

l1=list(set1)
print(l1)

#empty set
null_set=(), #note that here is no{} cuz that will make it a dictionary, it'll be strictly()