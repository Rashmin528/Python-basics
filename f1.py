#function call by different types
def add(x,y): #parameters
        sum = x + y
        return sum

result = add(4,5) #arguments
print("answer is" ,result)


def add(x,y,z):
        sum = x+y+z #parameters
        return sum

result = add(x=2,y=3,z=5) #arguments
print("answer is",result)

def add(*args):
        return args
a = add('2','3','4')
#python3 f1.py 
