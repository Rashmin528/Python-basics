#shallow copy
import copy

old = [1,2,3,4,5]
new = copy.copy(old)

print(old)
print(new)

#shallow copy with append
import copy

old = [1,2,4,5]
new = copy.copy(old)
old.append(3) #add to old list and change happen

print(old)
print(new)

#deep copy
import copy

old = [1,2,3,4,5]
new = copy.deepcopy(old)

print(old)
print(new)

#deep copy 
import copy

old = [1,2,4,5]
new = copy.deepcopy(old)
old.append(3) #add to old list and changes will not happen 

print(old)
print(new)
