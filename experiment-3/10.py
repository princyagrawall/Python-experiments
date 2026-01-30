"""Write a program to print the following pattern
123454321
1234 *4321
123 * * 321
12 * * * 21
1 * * * * 1"""

# Number of rows
n = 5

# Loop for each row
for i in range(1, n + 1):
    # Print the increasing numbers
    for j in range(1, n - i + 2):
        print(j, end='')

    # Print the stars
    for j in range(1, i):
        print(' *', end='')  # Add a space before * for formatting

    # Print the decreasing numbers
    for j in range(n - i + 1, 0, -1):
        print(j, end='')

    # Move to next line
    print()
