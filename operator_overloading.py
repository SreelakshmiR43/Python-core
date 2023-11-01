class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return point(x, y)

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)


p1 = point(1, 4)
p2 = point(4, 7)
print(p1 * p2)
print(p1 + p2)
