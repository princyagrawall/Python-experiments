"""Write a Python function to find the maximum and minimum numbers from a
sequence of numbers. (Note: Do not use built-in functions.)"""

def find_max_min(seq):
    maximum = seq[0]
    minimum = seq[0]

    for i in seq:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return maximum, minimum


n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

max_val, min_val = find_max_min(numbers)

print("Maximum:", max_val)
print("Minimum:", min_val)
