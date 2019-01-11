import copy

old = [1,2,3,4]
new = copy.copy(old)

print(old)
print(new)

#shallow copy
import copy

old = [[1,2,3,4],[1,2,3,4]]
new = copy.copy(old)
old[1][1] = 'R'

print(old)
print(new)

#deepcopy
import copy

old = [[1,2,3,4],[1,2,3,4]]
new = copy.deepcopy(old)

old[1][1] = 'Q'
print(old)
print(new)
