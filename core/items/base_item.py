from core.stats import Stats


class BaseItem:
    def __init__(self, stats=Stats(), name="Unnamed"):
        self.stats = stats
        self.name = name

    def __str__(self):
        return "[%s] (%s) %s" % (type(self),
                                 self.name,
                                 str(self.stats))
