#take user input a list and print length of list with function

#function for length
def measure_len(listname):
    length = len(listname)
    return length


n = int(input ("Enter how many elements you want to add : "))

l1 = []

for i in range(1,n+1):
    l1.append(input("Enter list element :"))

print("Your list is : ",l1)

length_of_list = measure_len(l1)
print("The length of your list is : ",length_of_list)


