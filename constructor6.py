#implementing method inside the constructor

class Employee:
    def __init__(self,name,salary):
        self.name   = name
        self.salary = salary

    def greeting(self):
        print("Hello",self.name)

emp1 = Employee("Omkar",60000)
emp2 = Employee("Sundarlal",30000)

emp1.greeting()