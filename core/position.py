class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%d, %d" % (self.x, self.y)

    def __add__(self, other):
        return Position(self.x + other.x,
                        self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x,
                        self.y + other.y)
