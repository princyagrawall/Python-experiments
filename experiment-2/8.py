"""Print the grade sheet of a student for the given range of cgpa. Scan marks of
five subjects and calculate the percentage.
CGPA=percentage/10
CGPA range:
0 to 3.4 -> F
3.5 to 5.0->C+
5.1 to 6->B
6.1 to 7-> B+
7.1 to 8-> A
8.1 to 9->A+
9.1 to 10-> O (Outstanding)
Sample Gradesheet
Name: Rohit Sharma
Roll Number: R17234512 SAPID: 50005673
Sem: 1 Course: B.Tech. CSE AI&ML
Subject name: Marks
PDS: 70
Python: 80
Chemistry: 90
English: 60
Physics: 50
Percentage: 70%
CGPA:7.0
Grade:"""

name = input("enter the name of student: ")
roll_number = input("enter the rol number of the student : ")
sapid = int(input("Enter the sapid of the student :"))
course = input("Enter the course of the student : ")
sem = int(input("Enter the sem of the student : "))

print("Enter the marks of the following subjects : ")
pds = int(input("PDS : "))
python = int(input("Python : "))
chemistry = int(input("Chemistry : "))
english = int(input("English : "))      
physics = int(input("Physics : "))

percentage = (pds + python + chemistry + english + physics) / 5
CGPA = percentage / 10

if CGPA >= 0 and CGPA < 3.4 :
    grade = 'F'
elif CGPA >= 3.4 and CGPA < 5.0 :
    grade = 'C+'
elif CGPA >= 5.1 and CGPA < 6 :       
    grade = 'B'
elif CGPA >= 6.1 and CGPA < 7.0 :
    grade = 'B+'
elif CGPA >= 7.1 and CGPA < 8.0 :
    grade = 'A'
elif CGPA >= 8.1 and CGPA < 9.0 :
    grade = 'A'
else :
    grade = 'O'

print("                                 Gradesheet")
print(f"Name :{name}")
print (f"Roll Number :{roll_number}                       SAPID:{sapid} ")
print(f"Sem:{sem}                                  Course :{course}\n")

print("Subject name: Marks\n")
print(f"PDS:{pds}")
print(f"Python:{python}")
print(f"Chemistry:{chemistry}")
print(f"English:{english}")
print(f"Physics:{physics}\n")


print(f"Percentage: {percentage}")
print(f"CGPA: {CGPA}")
print(f"Grade: {grade}")
