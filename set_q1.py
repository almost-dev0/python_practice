"""
You are given a list of subjects for students. Assume one classroom is required
for 1 subject. How many classrooms are needed?
"python","java","C++", "python","js","java","python","java","C++","C"
"""

#here we will use sets because this will delete duplicate values and tell us exact howan classes are there 

set_classes = {"python","java","C++", "python","js","java","python","java","C++","C"}
print(set_classes)

print("The no of classrooms required are :",len(set_classes))