"""
Create student class that takes name and marks of three subjects as arguments in constructor. 
Then create a method to print the average
"""

class Student:
    def __init__(self,name,phy_marks,chem_marks,maths_marks):
        self.name        = name
        self.phy_marks   = phy_marks
        self.chem_marks  = chem_marks
        self.maths_marks = maths_marks

    def calc_avg(self):
        avg =(self.phy_marks + self.chem_marks + self.maths_marks)/3
        return avg

s1 = Student("Narendra",80,90,85)
s2 = Student("Amit",90,80,95)

print("Average score of s1 is :",s1.calc_avg())

