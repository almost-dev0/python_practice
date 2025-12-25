"""
Create a Python class Student to store multiple students’ marks and calculate grades.

Constructor (__init__) should take: name (string), marks (integer)

Methods:
result() → Returns "Pass" if marks ≥ 40 else "Fail"

grade() → Returns grade based on marks:
90+ → "A+" | 80–89 → "A" | 70–79 → "B" |60–69 → "C" | 40–59 → "D" | Below 40 → "F"

display() → Prints: <name> has <Pass/Fail> with <marks> marks and grade <grade>

Create 3 students with marks:
Omkar → 95, Rohit → 72, Akash → 38

Call display() for all 3 students.
"""

class Student:
    def __init__(self,name,marks):
        self.name  = name
        self.marks = marks

    def result(self):
        if (self.marks >= 40):
            return "Passed"
        else:
            return "Failed"
        
    def grade(self):
        if (self.marks >= 90):
            return "A+"
        if (self.marks >=80 and self.marks <= 89):
            return "A"
        if (self.marks >=70 and self.marks <= 79):
            return "B"
        if (self.marks >=60 and self.marks <= 69):
            return "C"
        if (self.marks >=40 and self.marks <= 59):
            return "D"
        if (self.marks < 40):
            return "F"
        
    def display(self):
        print(self.name,"has",self.result(),"with","marks",self.marks,"and grade",self.grade())

s1 = Student("Omkar", 95)
s2 = Student("Rohit", 72)
s3 = Student("Akash", 38)

s1.display()
s2.display()
s3.display()

