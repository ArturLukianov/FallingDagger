class Stats:
	def __init__(self, attack=0, defence=0, hitpoints=0, _range=0):
		self.attack = attack
		self.defence = defence
		self.hitpoints = hitpoints
		self.range = _range
	
	def __str__(self):
		return "[Stats]: (atk: %d, def %d, hp: %d)" % (self.attack,
												self.defence)