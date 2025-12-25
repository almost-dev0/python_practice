#Create a Book class with constructor for title, author, price, then make two objects and print their titles.

class Book:
    def __init__(self,title,author,price):
        self.title  = title
        self.author = author
        self.price  = price

book1 = Book("Agnipankh","Dr APJ Abdul Kalam",200)
book2 = Book("One Arranged Murder","Chetan Bhagat",250)

print("Title of First Book is :",book1.title)
print("\nTitle of Second Book is :",book2.title)
