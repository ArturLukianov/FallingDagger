from stats import Stats

class BaseCharacter():
	def __init__(self, position, stats=Stats(), name="Unnamed", equipment=Equimpent):
		self.stats = stats
		self.name = name
		self.position = position
		self.inventory = []
		self.equipment = equipment
		
	def move_to(self, position):
		self.position = position
		
	def move(self, delta_position):
		self.position += delta_position
		
	def __str__(self):
		return "[%s] (%s) %s <%s>" % (type(self),
								self.name,
								str(self.stats),
								str(self.position))