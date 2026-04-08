class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(self.x, self.y)

p1 = Point(10, 20)
p2 = Point(12, 15)
p3 = p1 + p2

p3.display()