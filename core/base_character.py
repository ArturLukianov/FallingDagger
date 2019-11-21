from .stats import Stats
from .equipment import Equipment
from .inventory import Inventory
from .delta_position import DeltaPosition


class BaseCharacter:
    def __init__(self, position, angle=0, velocity=DeltaPosition(0, 0),
                 name="Unnamed", inventory=Inventory(), equipment=Equipment(), stats=Stats(), angle_velocity=0):
        self.stats = stats
        self.name = name
        self.position = position
        self.inventory = inventory
        self.equipment = equipment
        self.velocity = velocity
        self.angle = angle
        self.angle_velocity = angle_velocity

    def apply_velocity(self):
        self.position += self.velocity

    def move_to(self, position):
        self.position = position

    def move(self, delta_position):
        self.position += delta_position

    def get_stats(self):
        return self.equipment.sum_stats()

    def __str__(self):
        return "[%s] (%s) %s <%s>" % (type(self),
                                      self.name,
                                      str(self.stats),
                                      str(self.position))
