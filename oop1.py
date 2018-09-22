class Person(object): #class 

	Name = '' #class variable
	Age = 0  #class variable

	def __init__(self, Name, Age): #initialize class Attribute
		self.Name = Name #instance variable
		self.Age = Age

	def Display(self): #methods
		return Name
		return Age

p_1 = Person("Richmond",46) #class instance
p_2 = Person("Rashmin", 22) 

print(p_1.Name, p_1.Age)#output
print(p_2.Name, p_2.Age)#output
