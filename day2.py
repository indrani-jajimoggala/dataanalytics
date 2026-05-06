''' Variables - meaningfull name
---------------
To define a variable, we have 2 rules
1. Good way to define a variable(no error). We define variable with (A-Z,a-b,_).
2. Bad way to define a variable(will get error). We should not starts with (0-9, special symbols or charcters).
3. we should not use keywords as a variables.
'''

A=18
i=20
_i=19
i2=14
print(A)
print(i)
print(_i)
print(i2)

''' we shouldnot use spaces while declaring a variable
@i=4
i g=5
print(@i)
print(i g) '''

#declaring a variable with meaningful
# We are going use meaningfull words or name for defining variables.
num = 4
_num = 6
my_str = "indu"
print(num)
print(_num)
print(str)

#Assigning a multiple variables with multiple values

a,d,c=1,2,3
print(f" a={a},d={d},c={c}")
# print(f"\ta,\td,\tc")
print(f" a+d={a+d}")

'''Tokens
---------------------
Nothing but a small program in python to complete the task
'''
a,b,c = 5,6,7
print(a*b)

#keywords - resvered words or built-in functions -if,else,in,or
#identifiers are nothing but a keywords

'''comments - to explain the logic while writing a code
single line comments - This is used to explain about that particular line in the code and we can represent with (#)symbol
multi-line comments - To comment morethan single line we can use multi-line comment (""" """,''' ''' - that won't be consider by the cursor)'''

''' Boolen type - True, Flase
------------------------------------
this is used to find out the statement is True or False '''

boolen_a = 12
boolen_b = 14
print(boolen_a == boolen_b)
boolen_c = 12
print(boolen_a == boolen_c)

num = 7
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
