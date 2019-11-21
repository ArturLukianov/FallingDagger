class Inventory:
    def __init__(self, contents=None):
        if contents is None:
            contents = []
        self.contents = contents

    def __add__(self, other):
        if type(other) != Inventory and \
                type(other) != list:
            raise Exception("Error adding %s" % type(other))
        return Inventory(self.contents + other.contents)

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return '[Inventory] %s' % ', '.join([str(item) for item in self.contents])

    def pop(self, index):
        if index < 0 or index > len(self):
            raise Exception("Index out of range")
        self.contents.pop(index)
