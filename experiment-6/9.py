"""Write a program to create two lists and generate a dictionary with keys from
list1 and values from list2."""

n = int(input("Enter number of elements: "))

list1 = []
list2 = []

for i in range(n):
    a = input("Enter key: ")
    list1.append(a)

for i in range(n):
    b = input("Enter value: ")
    list2.append(b)

result = {}

i = 0
while i < n:
    result[list1[i]] = list2[i]
    i = i + 1

print(result)
