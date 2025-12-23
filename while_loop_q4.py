#search for a numebr x in this tuple using loop : (1,4,9,16,25,36,49,64,81,100)

t1 = (1,4,9,16,25,36,49,64,81,100)

n = int(input("Enter Number you want to Search : "))

i = 1
while i <= (len(t1)-1):
    if (n == t1[i]):
        print("Element found at index ",i)
        break
    i += 1
