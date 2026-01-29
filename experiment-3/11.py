n = int(input("Enter value of n: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + ( 1 / i )
print("Sum of the series is:", sum)
