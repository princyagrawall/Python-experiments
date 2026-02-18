#Scan n values in range 0-3 and print the number of times each value has occurred.

n = int(input("Enter how many values: "))

count0 = 0
count1 = 0
count2 = 0
count3 = 0

for i in range(n):
    num = int(input("Enter value (0-3): "))
    
    if num == 0:
        count0 += 1
    elif num == 1:
        count1 += 1
    elif num == 2:
        count2 += 1
    elif num == 3:
        count3 += 1

print("0 occurred", count0, "times")
print("1 occurred", count1, "times")
print("2 occurred", count2, "times")
print("3 occurred", count3, "times")
