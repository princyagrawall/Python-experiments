"""Write a program to swap two numbers without taking additional variable."""
#method 1
a=5
b=10
a=a+b
b=a-b
a=a-b
print(a,b)

#method 2
a=10
b=20
c=b
b=a
a=c
print(a,b)