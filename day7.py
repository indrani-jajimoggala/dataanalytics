'''
Set()
it is collection of unordered elements or unique elements unlike list or tuple set is not permit duplicates in side.
it is mutable
methods:
add() - used for add new item into the set.
syntax: var_name.add()

remove();
delete the item in a set
syntax: var_name.remove(value)

pop():
delete the item in a set, but we can not specify the element
syntax: var_name.pop(no arguments)

clear():
delete all elements in the set

update()
same like add, but this method will add more than one element
syntax: var_name.update([elements])

union(): return a set all elements from both sets, but not duplicates.
syntax : set_1.union(set_2) or set_1 | set_2

intersection():
gives only common elements from both sets
syntax: set_1.intersection(set_2) or set_1 & set_2

difference():
different elements from the both sides
syntax: set_1.difference(set_2) or set_1 - set_2

sn = {1,2,3,2}
sn.add(4)
print(sn)
sn.update([6,7,8])
print(sn)
h = {6,9,8,2}
print(sn.union(h))
print(sn)
print(sn.intersection(h))
print(sn)
print(sn.difference(h))
print(sn - h)
'''

'''TYPE COVERTIONS:
Converting one datatype into another datatype
'''
a= 45
b = str(a)
print(b)
c = float(b)
print(c)
k = "47"
d = list(k)
print(d)
e = tuple(k)
print(e)
