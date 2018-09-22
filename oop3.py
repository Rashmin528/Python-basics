class Person:    
    Name = ''
    Age = 0

    def __init__(self, Name, Age):  
        self.Name = Name  
        self.Age = Age  
    
    def GetName(self):  
        print(self.Name)

    def GetAge(self):
        print(self.Age)    
  
class Student:   
    Id = ''
   
    def __init__(self, Id):  
        self.Id = Id  
  
    def GetId(self):  
        print(self.Id)  
  
  
class Resident(Person, Student):   
    one = ''   

    def __init__(self, Name, Age, Id):  
        Person.__init__(self, Name, Age)  
        Student.__init__(self, Id)  
    
  
resident1 = Resident('Rashmin', 22, '2')  
resident1.GetName()
resident1.GetAge()
resident1.GetId()  

