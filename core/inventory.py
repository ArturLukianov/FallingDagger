class Inventory:
	def __init__(self, contents):
		self.contents = contents
		
	def __add__(self, other):
		if type(other) != Inventory:
			raise Exception()
		