#Create a tuple to store n numeric values and find average of all values

n = int(input("Enter number of values: "))

values = ()

for i in range(n):
    num = float(input("Enter number: "))
    values = values + (num,)   

total = 0

for i in values:
    total += i

average = total / n

print("Tuple:", values)
print("Average:", average)
