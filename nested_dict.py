#nested dictionary means a dictionary as value of a key inside a dictionary

dict1={
    "name" : "Omkar",
    "age" : 22,
    "score" : {
                "physics" : 90,
                "chemistry" : 85,
                "cs"    : 99
              }
}

print(dict1)
print(dict1["name"])



#accessing elements of nested dictionary

print(dict1["score"]["physics"])    #two seperate square brackets,key->key 
                                    #syntax : print(dictname[key][inside_key])