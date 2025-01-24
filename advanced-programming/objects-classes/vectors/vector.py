import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y
 
    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def multiply(self, vector):
        return Vector(self.x * vector.x, self.y * vector.y)

    def dot_product(self, vector):
        return (self.x * vector.x) + (self.y * vector.y)

    def magnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def scalar_multiply(self, n):
        return Vector(n * self.x, n * self.y)



if __name__ == '__main__':
    v1 = Vector(3, 2)
    v2 = Vector(1, 1)
    v3 = Vector(4, 3)
    v4 = Vector(12, 6)
    v5 = Vector(20, 15)

    assert v1.add(v2) == (v3)
    assert v1.multiply(v3) == (v4)
    assert v1.dot_product(v3) == 18
    assert v2.magnitude() == math.sqrt(2)
    assert v3.scalar_multiply(5) == v5
    print("ok")
