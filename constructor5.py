#Create a Laptop class with constructor for brand,ram,price and thenmake two laptop objects and print their RAM

class Laptop:
    def __init__(self,brand,RAM,price):
        self.brand = brand
        self.RAM   = RAM
        self.price = price

l1 = Laptop("Acer Nitro","12 GB","70000")
l2 = Laptop("Asus ROG","16 GB","80000")

print("RAM of laptop 1 :",l1.RAM)
print("RAM of laptop 2 :",l2.RAM)