"""Add few names, one name in each row, in “name.txt file”.
a. Count no of names
2. b. Count all names starting with vowel
c. Find longest name"""

with open("name.txt", "w") as f:
    f.write("Ankit\n")
    f.write("Priya\n")
    f.write("Om\n")
    f.write("Riya\n")
    f.write("Aman\n")

with open("name.txt", "r") as f:
    names = f.readlines()

names = [name.strip() for name in names]

count_names = len(names)
print("Total names:", count_names)

vowels = ('A', 'E', 'I', 'O', 'U')
vowel_count = sum(1 for name in names if name.upper().startswith(vowels))
print("Names starting with vowel:", vowel_count)

longest_name = max(names, key=len)
print("Longest name:", longest_name)