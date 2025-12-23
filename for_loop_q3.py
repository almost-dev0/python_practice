#search for a number user input x from this tuple using for loop : (1,4,9,16,25,36,49,64,81,100)

t1 = (1,4,9,16,25,36,49,64,81,100)

n = int(input("Enter the number you want to search : "))

i = 0
for num in t1:
    if(num == n):
        print("Element found at index :",i)
        break;
    i += 1
else:
    print("Element not found")