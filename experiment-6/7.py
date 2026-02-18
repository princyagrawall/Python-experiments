"""Write functions to explain mentioned concepts:
a. Keyword argument
b. Default argument
c. Variable length argument"""

def keyword_example(name, age):
    print("Name:", name)
    print("Age:", age)

keyword_example(age=20, name="Princy")

def default_example(name, city="Delhi"):
    print("Name:", name)
    print("City:", city)

default_example("Riya")
default_example("Aman", "Mumbai")

def variable_length_example(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print("Sum:", total)

variable_length_example(10, 20)
variable_length_example(5, 15, 25, 35)
