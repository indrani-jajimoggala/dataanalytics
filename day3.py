#Operators
#Arithmetic Operator
a=int(input("enter a number:"))
b=int(input("enter b number:"))
print(f"addition of two numbers:{a+b}")
print(f"subtraction of two numbers:{a-b}")
print(f"multiple of two numbers:{a*b}")
print(f"division of two numbers:{a/b}")
print(f"module of two numbers:{a//b}")
print(f"expo of two numbers:{a**b}")

#Assignment Operator (=,+=,-=,*=,/+,//=,%=)
num3 = 4
num3 += 2  #num3 = num3+2    --> num3= 4+2  --> num3 = 6
print(f"Assignment Operator: {num3}")

#Comparsion Operator(>,<,>=,<=,==,!=)
num4 = 16
num5 = 7
print("Comparsion Operator")
print(num4 > num5)
print(num4 < num5)
print(num4 >= num5)
print(num4 <= num5)
print(num4 == num5)
print(num4 != num5)

#and --> the 2 conditions should be true
v = 8
n = 78
print("Logical operators")
print(f"and:{v < 10 and n > 10}")
print(f"or: {v < 10 or n > 10}")
print(f"not: {not(v < 10 and n > 10)}")  #to reverse the operator


#identity operators (is, isnot)-- this is used for check the object of the variable
y = 6
z = 6
print("identity operator")
print(id(y))
print(id(z))

list = [1,2]
list_2 = [1,2]
list_3 = list
print(id(list))
print(id(list_2))
print(id(list_3))
print(list==list_2)
print(list is list_2)
print(list is not list_2)

#membership operators (in - used for to check, it present init. not in)
list1 = [1,2]
print(f"membership operator")
print( 2 in list1)
print( 2 not in list1)

#bitwise operators: &,|,^,~,<<,>>
#& - bitwise and, |-bitwise or, ^-xor
'''5 --> 0101
   3 --> 0011
   -----------
   1 --> 0001 '''
print(5&3)  #1(0001)
print(5^3)  #6(0110)
print(5|3)  #7(0111)
