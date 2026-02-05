"""Write a program to count and display the number of capital letters in a given
string."""

string = input("Enter a string: ")
count = 0
print("Capital letters:")
for char in string :
    if char.isupper():
      print(char,end=" ")  
      count += 1

print("\nnumber of capital letters in string : ",count)

