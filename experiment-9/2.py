class Student:
    def __init__(self, name, sap, phy, chem, maths):
        self.name = name
        self.sap = sap
        self.marks = [phy, chem, maths]

    def display(self):
        print(self.name, self.sap, self.marks)

    def marks_percentage(self):
        return sum(self.marks) / 3

    def result(self):
        if all(m > 40 for m in self.marks):
            print("Pass")
        else:
            print("Fail")

def class_average(students):
    total = 0
    for s in students:
        total += s.marks_percentage()
    return total / len(students)

n = int(input())
students = []

for i in range(n):
    name = input()
    sap = input()
    phy = int(input())
    chem = int(input())
    maths = int(input())
    students.append(Student(name, sap, phy, chem, maths))

for s in students:
    s.display()
    print(s.marks_percentage())
    s.result()

print(class_average(students))