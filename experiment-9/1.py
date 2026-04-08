class Student:
    def __init__(self, name, sap, phy, chem, maths):
        self.name = name
        self.sap = sap
        self.marks = [phy, chem, maths]

    def display(self):
        print(self.name, self.sap, self.marks)

students = []

for i in range(3):
    name = input()
    sap = input()
    phy = int(input())
    chem = int(input())
    maths = int(input())
    s = Student(name, sap, phy, chem, maths)
    students.append(s)

for s in students:
    s.display()