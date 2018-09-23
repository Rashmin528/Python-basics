#@classmethod and @staticmethod
class Pizza:
	def __init__(self,ingredients):
		self.ingredients = ingredients
	
	@classmethod
	def mexican(cls, veg):
		return cls(veg)

	@classmethod
	def italian(cls, non_veg):
		return cls(non_veg)

one = Pizza.mexican('onion')
two = Pizza.italian('chicken')
print(one.ingredients)
print(two.ingredients)

