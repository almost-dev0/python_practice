#write a function to convert usd to inr

def currency_conv(usd):
    inr = usd * 90
    return inr

usd = int(input("Enter USD value : "))

inr = currency_conv(usd)
print("The value of",usd,"USD in INR is : Rs",inr)