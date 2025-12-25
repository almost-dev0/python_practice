"""
Create a Python class named Student to store and display student result details.
The class should have a constructor that takes: name (student name), marks (integer)

The class should have a method result() that:   |   The class should have another method display() that:
Returns "Pass" if marks are 40 or above         |   Calls the result() method
Returns "Fail" if marks are below 40            |   Prints o/p format: <name> has <Pass/Fail> with <marks> marks

Create two objects of the Student class with the following data:
Student 1: Omkar, 78 marks
Student 2: Rohit, 32 marks

Call the display() method for both students.
"""

class Student:

    def __init__(self,name,marks):
        self.name  = name
        self.marks = marks

    def result(self):
        if(self.marks >= 40):
            return "Passed"
        else:
            return "Failed"

    def display(self):
        print(self.name,"has",self.result(),"with marks :",self.marks)

s1 = Student("Omkar",78)
s2 = Student("Rohit",32)

s1.display()
s2.display()
