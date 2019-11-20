class Stats:
	def __init__(self, attack=0, defence=0):
		self.attack = attack
		self.defence = defence
	
	def __str__(self):
		return "[Stats]: (atk: %d, def %d)" % (self.attack,
												self.defence)