"""Given a string containing both upper and lower case alphabets. Write a Python
program to count the number of occurrences of each alphabet (case
insensitive) and display the same.
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G"""

s = input("Enter a string: ")
s = s.upper()

used = ""

for i in s:
    if i.isalpha() and i not in used:
        count = 0
        for j in s:
            if i == j:
                count += 1
        print(str(count) + i)
        used += i
