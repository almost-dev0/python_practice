#take 5 elements from user, and check if list is palindrome

l1 = []
l1.append(input("Enter first element :"))
l1.append(input("Enter second element :"))
l1.append(input("Enter third element :"))
l1.append(input("Enter fourth element :"))
l1.append(input("Enter fifth element :"))

print("Your list is : ",l1)

l2 = l1.copy()
l2.reverse()

if(l1 == l2):
    print("List is palindrome")
else:
    print("List is not palindrome")