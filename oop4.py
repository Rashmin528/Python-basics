class Student(object): #class
	
	id = '' #class variable
	name = ''
	
	def __init__(self): #construct
		self.id = '6262' #instance variable attribute
		self.name = 'Rashmin'

student = Student()#class instance
print(student.id,student.name)

print(getattr(student,"cgpa", 7.04) #getattr is calling without init in constructors

