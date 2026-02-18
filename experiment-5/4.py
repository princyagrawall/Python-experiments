"""Create a dictionary of n persons where key is name and value is city.
a) Display all names
b) Display all city names
c) Display student name and city of all students.
d) Count number of students in each city"""

n = int(input("Enter number of persons: "))

data = {}


for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    data[name] = city


print("Names are:")
for i in data:
    print(i)


print("Cities are:")
for i in data:
    print(data[i])


print("Name and City:")
for i in data:
    print(i, "-", data[i])


count = {}

for i in data:
    city = data[i]
    if city in count:
        count[city] = count[city] + 1
    else:
        count[city] = 1

print("Number of students in each city:")
for i in count:
    print(i, "-", count[i])
