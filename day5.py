'''
list[]:
List is collection of different datatypes and it is represent by [].
It is mutable datatype.

any = [1,"hi",[2,3]]
print(any)   #[1, 'hi', [2, 3]]
g = [1,"Python is a language",[2,"this is 5th class",7],89]
print(g[2])  #[2, 'this is 5th class', 7]
print(g[2][1])     #this is 5th class
print(g[2][1][10]) #h

j = [1,"Python is a language",67,68,[34,"This is python class",78,"I'm looking for good bat"],[2,"this is 5th class",3],56]
print(j[4])      # [34, 'This is python class', 78, "I'm looking for good bat"]
print(j[4][1])   # This is python class
print(j[4][1][15])   #c

i = [1,"Python is a language",67,68,[34,["This is python class"],78,"I'm looking for good bat"],[2,"this is 5th class",3],56]
print(i[4])     #[34, ['This is python class'], 78, "I'm looking for good bat"]
print(i[4][1])  #['This is python class']
print(i[4][1][0])  #This is python class
print(i[4][1][0][15])  #c



methods: 1.append, 2.extend, 3.pop, 4.remove 5.clear 6.copy 7.insert 8.reverse

append() - add a new item into list, but it will add in the index position.
syntax : variable_name.append(position of the item)
an = [1,2,3,4]
an.append(4)
print(an)   #[1, 2, 3, 4, 4]
#if you want to add 2 more items in  the list then we have create the new list in the existing list.
an.append([8,9])
print(an)   #[1, 2, 3, 4, 4, [8, 9]]


extend() - used to add new item into list but this extend add as each position to each index in the list.
extend only takes iterables.
syntax : var_name.extend(item(iterable))

an.append("python")
print(an)      #[1, 2, 3, 4, 4, [8, 9], 'python']
an.extend("python")
print(an)      #[1, 2, 3, 4, 4, [8, 9], 'python', 'p', 'y', 't', 'h', 'o', 'n']

#pop():it deletes the index position of the item in the list. if nothing is mentioned in the parameters it will remove last index position
#syntax : var_name.pop(index_position)
an.pop(2)
print(an)      #[1, 2, 4, 4, [8, 9], 'python', 'p', 'y', 't', 'h', 'o', 'n']

#remove(): it removes the item from list,but remove() method will delete direct value without checking the index position
#syntax : var_name.remove(value)
an.remove(4)   #[1, 2, 4, [8, 9], 'python', 'p', 'y', 't', 'h', 'o', 'n']
print(an)

#slicing[:] or [::] : var_name[start index: stop index]
h = [1,2,3,4,5]
print(h[1:4])   #[2, 3, 4]

#len() : Used to find the number of items present in the list
#syntax: len(var_name)
o = "Python is a langauge"
print(len(o))

#insert():
'''
an = [1,2,3,4]
an = an + [5,6,7,8]
print(an)
print(an[6])   #accessing the particular value by the giving or using the position
an[6] = "hi"  #replacing the value 7 with hi with using position
print(an)
an.append(9)  #append means adding an element in the end of the list
print(an)
print(len(an))
#print(an*5)
print(an[1]*4)


