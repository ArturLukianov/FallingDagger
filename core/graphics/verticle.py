from math import sqrt


class Verticle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if type(other) != Verticle:
            raise Exception("Cannot add not <Verticle>")
        return Verticle(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)

    def __sub__(self, other):
        if type(other) != Verticle:
            raise Exception("Cannot subdivide not <Verticle>")
        return Verticle(self.x - other.x,
                        self.y - other.y,
                        self.z - other.z)

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 +
                    (self.y - other.y) ** 2 +
                    (self.z - other.z) ** 2)
