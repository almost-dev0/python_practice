"""
WAP to enter marks of 3 subs from user and store them in dictionary. Stat with empty
dictionary and ad one by one . Use subject name as key and marsk as values
"""

dict = {}
print(dict)

m1 = int(input("Enter marks of physics     : "))
dict.update({"physics" : m1})

m2 = int(input("Enter marks of chemistry   : "))
dict.update({"chemistry" : m2})

m3 = int(input("Enter marks of mathematics : "))
dict.update({"mathematics" : m3})

print(dict)