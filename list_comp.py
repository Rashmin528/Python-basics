#list comprehension
#LAMBDA
a = lambda x,y : x if x>y else y
print(a(2,5))

#MAP
n = [1,2,3,4,5]
print(list(map(lambda x: x**2,n)))

#FILTER
n = [1,2,3,4,5]
print(list(filter(lambda x: x>3,n)))

#REDUCE
n = [1,2,3,4,5]
print(reduce(lambda x,y: x+y,n))

