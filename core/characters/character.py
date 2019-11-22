from core.characters.base_character import BaseCharacter
from core.ai.base_ai import BaseAI
from core.stats import Stats
from core.items.equipment import Equipment
from core.items.inventory import Inventory
from core.characters.delta_position import DeltaPosition


class Character(BaseCharacter):
    def __init__(self, position, angle=0, velocity=DeltaPosition(0, 0),
                 name="Unnamed", inventory=Inventory(), equipment=Equipment(), stats=Stats(), angle_velocity=0,
                 ai=None):
        super().__init__(position, angle, velocity, name, inventory, equipment, stats, angle_velocity)
        self.ai = ai

    def set_ai(self, new_ai):
        self.ai = new_ai
