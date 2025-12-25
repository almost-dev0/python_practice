"""
Create a Python class Rectangle with the following:
Constructor (__init__) should take: length, breadth

Methods:
area() → Returns area of rectangle      |       perimeter() → Returns perimeter of rectangle
display() → Prints: Rectangle with length <length> and breadth <breadth> has area <area> and perimeter <perimeter>


Create 2 rectangles:
Rectangle 1 → 5, 10
Rectangle 2 → 7, 3

Call display() for both rectangles.
"""

class Rectangle:
    def __init__(self,length,breadth):
        self.length  = length
        self.breadth = breadth
    
    def area(self):
        area = self.length * self.breadth
        return area
    
    def perimeter(self):
        perimeter =  2 * (self.length + self.breadth)      
        return perimeter
    
    def display(self):
        print("Rectangle with",self.length,"and",self.breadth,"has area",self.area(),"and perimeter",self.perimeter())

rect1 = Rectangle(5,10)
rect2 = Rectangle(7,3)

rect1.display()
rect2.display()