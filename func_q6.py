#write a fucntion to print the elements of a list ina a single line(list is the parameter)
def print_listels(lst):
    for elements in lst:
        print(elements, end = " ")


l1 = []
n = int(input("Enter no. of elements in your list :"))

for i in range (1, n+1):
    l1.append(input("Enter element:"))

print_listels(l1)
