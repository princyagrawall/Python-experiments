"""Find the greatest among the two numbers. If numbers are equal than print
“numbers are equal”."""
num1 =int(input("enter num1 : "))
num2 =int(input("enter num2 : "))

if num1 > num2 :
    print("num1 is greater")
elif num1 < num2 :
    print("num2 is greater")
else :
    print("Both are equal")