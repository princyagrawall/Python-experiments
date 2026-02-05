#Count total number of vowels in a given string.
 
string=input("Enter a string: ")
count=0
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels :
     print(char)
     count += 1

print("number of vowels in given string is ",count)