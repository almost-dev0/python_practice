std_info = {
    "name"      : "Omkar",
    "age"       : "25",
    "course"    : "MCA",
    "category"  : "General",
    "cgpa"      : "7.25",
    "subjects"  : ["java","python","research project"],
    "grades"    : ('a','b', 'c')
}

#dictname.keys(), returns all keys
print(std_info.keys())

#dictname.values(), returns all values
print(std_info.values())

#dictname.items(), returns all (key,values) pairs as keys
print("\n",std_info.items())

#dictnam.get("key"),returs value according to key, used in industry because if key doesn't exists, simply print none and also runs rest of the code
print(std_info.get("city"))
print(std_info.get("cgpa"))

#dictname.update(), update values n key
std_info.update({"city" : "Rahuri"})
print(std_info)