str1 = input("Enter First string :")
str2 = input("Enter Second string :")

#concatenation
str3 = str1+str2
print("Output String is ",str3)

#length of string
print("length of first string : ",len(str1) )
print("length of second string : ",len(str2) )
print("length of third string : ",len(str3) )


#str.endswith(""), returns true if string ends with substring given inside " "
print(str.endswith("ech"))
print(str.endswith("h"))
print(str.endswith("HFP"))

#stringname.capitalize(), capitalise first char of string
string1 = "hfptech"
print(string1.capitalize())

#stringname.replace(old,new), replaces old with new
string2 = "sea and seasons"
print(string2.replace("s","p"))

#stringname.count, count occurences of substring
string3 = "sea and seasons"
print(string3.count("se"))
print(string3.count("s"))
print(string3.count("p"))