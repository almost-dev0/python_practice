#Create a Student class with constructor for name, grade, roll_no, then make two student objects and print their grades.

class Student:
    def __init__(self,name,grade,roll_no):
        self.name    = name
        self.grade   = grade
        self.roll_no = roll_no

s1 = Student("Omkar","A",96)
s2 = Student("Ritesh","B",108)

print("Grades of s1 : ",s1.grade)
print("Grades of s2 : ",s2.grade)
