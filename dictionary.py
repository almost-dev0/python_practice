#creating a dictionary
std_info = {
    "name"      : "Omkar",
    "age"       : "25",
    "course"    : "MCA",
    "category"  : "General",
    "cgpa"      : "7.25",
    "subjects"  : ["java","python","research project"],
    "grades"    : ('a','b', 'c')
}
print(std_info)
print(type(std_info))



#accessing dictionary through keys
print(std_info["name"])
print(std_info["age"])
print(std_info["cgpa"])
print(std_info["subjects"])   


#changing values (mutability)
std_info["name"] = "Abhi"
print(std_info)

#we can also create a null dictionary
null_dict = {}
print(null_dict)

