"""Write a lambda function to find volume of cone."""
volume = lambda r, h: (3.14159 * r * r * h) / 3

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Volume of cone:", volume(r, h))
