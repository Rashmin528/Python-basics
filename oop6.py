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
	
	@staticmethod
	def isBill(price):
		return 500 > price 

one = Pizza.mexican('onion')
two = Pizza.italian('chicken')
print(one.ingredients)
print(two.ingredients)
print(Pizza.isBill(450))

