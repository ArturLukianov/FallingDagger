from math import sqrt


class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if type(other) != Vertex:
            raise Exception("Cannot add not <Vertex>")
        return Vertex(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        if type(other) != Vertex:
            raise Exception("Cannot subdivide not <Vertex>")
        return Vertex(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __str__(self):
        return '%d, %d, %d' % (self.x, self.y, self.z)

    def __repr__(self):
        return str(self)

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 +
                    (self.y - other.y) ** 2 +
                    (self.z - other.z) ** 2)

    def to_list(self):
        return self.x, self.y, self.z

    def copy(self):
        return Vertex(self.x, self.y, self.z)
