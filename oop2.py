class Person(object): #class

	Name = '' #class variable
	Age = 0

	def __init__(self, Name, Age): #instance variable  
		self.Name = Name 
		self.Age = Age

	def display(self): #methods
		print(self.Name)
		print(self.Age)

class Student(Person): #multiple inheritence (class)
	
	Id = '' #class variable  

	def __init__(self, Id):  #instance variable
		self.Id = Id
	
	def display(self): #methods
		print(self.Id)

p_1 = Person("Rashmin", 22) #class instance
p_2 = Student("5f6sd")

print("Name:",p_1.Name) #output
print("Age:",p_1.Age) 
print("Id:",p_2.Id)
