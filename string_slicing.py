str = "HFPTech"

#accessing elements of string through index
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])

#slicing : 
#positive- 0 to len(str)
#negative- -(strlen) to -1
print(str[1 : 4])
print(str[0 : 3])
print(str[0 :  ])        #blank space after first index means it'll go till last index
print(str[  : 5])        #blank space before second index means it'll start from 0th index
print(str[4 : 1])        #if input index first>second, blank output   
print(str[-7: -4])         #negative index starts from -1 at last element, no zero included
print(str[-5:  ])         #negative index starts from -1 at last element, no zero included
print(str[-5:  2])         # negativ to positive not allowed, blank output

