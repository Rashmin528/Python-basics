 class Person: #class    
    Name = ''# class variable
    Age = 0

    def __init__(self, Name, Age): #construct  
        self.Name = Name  #instance variable attri
        self.Age = Age

    def GetName(self):  #methods
        print(self.Name)

    def GetAge(self):
        print(self.Age)

class Student: #class
    Id = '' #class variable

    def __init__(self, Id): #construct  
        self.Id = Id  #instance variable

    def GetId(self):  #methods
        print(self.Id)


class Resident(Person, Student): #multiple inheritence   

    def __init__(self, Name, Age, Id):
        Person.__init__(self, Name, Age)
        Student.__init__(self, Id)


resident1 = Resident('Rashmin', 22, '2')  #class instance or object of an instance
resident1.GetName()#ouput
resident1.GetAge()
resident1.GetId()


