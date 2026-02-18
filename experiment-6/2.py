"""Write a Python function that takes a positive integer and returns the sum of the
cube of all the positive integers smaller than the specified number."""

def sum_of_cubes(n):
    total = 0
    i = 1
    while i < n:
        total = total + (i * i * i)
        i = i + 1
    return total

num = int(input("Enter a positive integer: "))
result = sum_of_cubes(num)
print(result)
