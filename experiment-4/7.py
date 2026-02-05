""""Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a) Fruits which are in both sets s1 and s2
b) Fruits only in s1 but not in s2
c) Count of all fruits from s1 and s2"""

s1= set(input("enter elements of set1: " ).split())
s2= set(input("enter elements of set2: " ).split())

print("set1: ",s1)
print("set2 : ",s2)

print("union",s1|s2)
print("Intersection",s1&s2)
print("difference ",s1-s2)
print("difference ",s2-s1)
print("symmetric difference",s1^s2)