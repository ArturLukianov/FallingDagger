from .graphics.vertex import Vertex

class Position:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "%d, %d, %d" % (self.x, self.y, self.z)

    def __add__(self, other):
        return Position(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)

    def __sub__(self, other):
        return Position(self.x - other.x,
                        self.y + other.y,
                        self.z + other.z)

    def to_vertex(self):
        return Vertex(self.x, self.y, self.z)
