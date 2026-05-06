''' 7 8 9
User input():


any = int(input("enter a number: "))
print(type(any))

#list datatype
a = list(map(int,input("enter list numbers: ").split()))
print(a)
print(type(a))

#tuple datatype
b = tuple(map(int,input("enter tuple numbers: ").split()))
print(b)
print(type(b))

if statement:
this is used to check condition is true or not

an = 9
if an == 9:
    print(f"an equal to {9}")

else:
it is fall-back stmt, incase if statement becomes false, it will enter into else.
an = 9
if an == 9:
    print(f"an equal to {9}")
else:
    print(f"an is not greaterthan {9}")'''

'''
g=100
if g <= 98:
    print(f"g equal to {98}")
else:
    print(f"g is greaterthan {98}")'''

'''
num = 9
num1 = 5
if num>num1:
    print(f"{num} is greaterthan {num1}")
else:
    print(f"{num1} is greaterthan {num}")

marks = 78
if marks > 90:
    print("A+")
if marks > 80:
    print("B+")
if marks > 70:
    print("C+")
else:
    print("F+")
'''

name = "python"

if name == "c" or "cc":
    print("login valid")
else:
    print("not valid")


number = 56
if number%2==0:
    print("even")
else:
    print("odd")

a = (1,2)
a = a + (3,)
print(a)

str = "mam"
count = 0
for i in str:
    

    
