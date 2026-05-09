'''
def great (name):
    print(f"Hello {name}")
great("indu")

def add(a,b):
    return a+b
result = add(7,8)
print(result)
#print: shows the output on the screen
#return: sends a value back to the caller or calling for the program to reuse

built-in functions:
len()-used to find the length of the variable,
max()- used to find the max number in the variable,
min()- used to find the min number in the variable,
sort()- sorts the elements in ascending or decending order,
avg()- used to find the avg number in the variable,
sum()- used to find the total number in the variable
type()- find the datatype stored in the variable.
m = ("python",78,79,456,"language")
print(max(m)) #error:type error
recursive function: function calls itself.

def fac(num):
    if num==0 or num==1:
        return 1
    return num*fac(num-1)
print(fac(4))'''


def table(num):
    for i in range(num):
        print(num,"X",i,"=",num*i)
table(5)

#error: execution stops
#bug: execepted result won't come
