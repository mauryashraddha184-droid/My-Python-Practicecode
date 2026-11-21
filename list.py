# adding item to list
#append
from requests import delete


L = [1,2,3,4,5]
L.append(True)
print(L)
#extend
L.extend([7,8])
print(L)
#insert
L.insert(2,1)
print(L)

#deleting items from list
#remove
L1=[1,2,2,3,4,5,6]
L1.remove(4)
print(L1)
#delete
del L1[1:3]
print(L1)
#pop
L1.pop(2)
print(L1)
#clear
L1.clear()
print(L1)

#operation on list
#concatination
L2=[1,2,3,4,5,6]
L3=[7,8,9,10]
L4=L2+L3
print(L4)
#multiplication
print(L2*3)
# membership
print(5 not in L2)
#common function in list
L5=[1,2,3,4,4,5]
print(len(L5))
print(max(L5))
print(min(L5))
print(sorted(L5))

