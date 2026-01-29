num = int(input("Enter a number: "))
shift = int(input("Enter number of shifts: "))
leftshift = num  << shift
rightshift = num >> shift
print ("Left shift value =", leftshift)
print("Right shift value =", rightshift)