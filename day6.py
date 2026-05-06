'''
tuples and dictionaries
tuple is mutable. when tuple is created we cann't modify the elements. represented with ()'''

e = (1,2,3,4)
print(e)
print(type(e))
j = 1,2,3,4
print(type(j))
print(f"addition of e & j:{e+j}"," - "," (+) it works as a concatation")
print(f"e==j is {e==j}")
print(f"e is j : {e is j}")

r = 12
f = 12
print(f"r==f is {r==f}")
print(f"r is f : {r is f}")

g = 6789
s = 6789
print(f"g==s is {g==s}")
print(f"g is s : {g is s}")

k = (1,2,3,4)
u = tuple([1,2,3,4])   # created at runtime
print(f"k==u : {k==u}")
print(f"k is u : {k is u}")

so = (1,"python",[7,8],(5,0),1)
print(so[1])


#dict(): dic is a collection of key : value pair, where keys are immutable(str, int, tuple) and value are any datatype. This is represented by {key : value}.
'''
methods:
key()-only keys needed
syntax: dict.keys()

value()-only values needed
syntax: dict.values()

items()- print key paired values.
syntax: dict.items()

clear()- to clear the key value paired.
syntax: dict.clear()

update()- add info
syntax: var_name.update({k : v}) '''

my = {"Name" : "Teja","age" :56,"Edu":"B.Tech"}
print(my.keys())
print(my.values())
print(my.items())
my.update({"Role" : "DA"})
print(my)

