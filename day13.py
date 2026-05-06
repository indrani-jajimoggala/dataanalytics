'''
function() : It is a block of code that can be reusable.
function can only run when it is called.
def is keyword used to define the function
def : defination of the function
syntax:
def fun_name(parameters):
    ----------
    ----------
    ----------

fun_name(arguments)  --- calling fun

required aruments:
function was called with the correct number of arguments, that means if function excepts 2 arguments, we have to call function with 2arguments not less or more.

Default arguments:
by, default, value is taken from calling function only.

Keyword Arguments:
Here, we can send arguments with key=value syntax. By this, the order of arguments does not matter.

variable length  argument:
adding a (*) star before the parameter name in the function, recieve a tuple of arguments and can be access items with indexes.

'''
num = 6
def even_odd(num):
    if num % 2==0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
even_odd(num)

def even_odd(num1,num2):
    print(num1+num2)
even_odd(6,7)

def even_odd(name="indu"):
    print(f"hai {name}")
even_odd("rani")
even_odd()

def even_odd(num,num1,num2):
    print(num+num1+num2)
even_odd(num2=9,num=6,num1=4)

def even_odd(*name):
    print(name[1])
even_odd("rani","indu","devi")
