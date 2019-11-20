from stats import Stats

class BaseItem:
	def __init__(self, stats=Stats(), name="Unnamed"):
		self.stats = stats
		self.name = name
	
	def __str__(self):
		return "[BaseItem] (%s) %s" % (self.name,
										str(self.stats))