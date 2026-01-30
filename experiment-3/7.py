"""Count and print all numbers divisible by 5 or 7 between 1 to 100."""
count = 0
for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(i)
        count = count + 1

print("Total count:", count)
