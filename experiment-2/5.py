"""Check whether the quadratic equation has real roots or imaginary roots.
Display the roots."""
import math
a = float(input("enter value of a:"))
b = float(input("enter value of b:"))
c = float(input("enter value of c:"))

d = (b**2) - (4*a*c)

if d > 0 :
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    print(f"Roots are real and different : {root1} and {root2}")

elif d == 0 :
    root = -b/(2*a)
    print(f"Roots are real and same: ",{root})

else :
    real = -b/(2*a)
    imag = math.sqrt(-d)/(2*a) 
    print("Roots are imaginary:" )
    print(f"{real} + {imag}i")
    print(f"{real} - {imag}i")
