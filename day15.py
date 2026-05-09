'''def fibonaaci(num):
    if num <= 1:
        return 1
    return fibonaaci(num-1)+ fibonaaci(num-2)

num = 0
num_1=1
any = int(input("enter a number: "))
#print(num,num_1,end=" ")
for i in range(1,any+1):
    num2=num+num_1
    num=num_1
    num_1=num2
    print(num2,end=" ") 

Amstrong_ = int(input("enter a number: ")
total = 0
length_ = len(str(Amstrong_))
for j in str(Amstrong_):
    total+=int(j)**length_
if total == Amstrong_:
    print(f"{Amstrong_} is amstrong number")
else:
     print(f"{Amstrong_} is not amstrong number") 

num=17
if num%3==0 and num%5==0:
    print(f"{num} is div by 3&5")
else:
    print(f"{num} is not div by 3&5")

any = [34,67,56,2,3,7]
def sum_even(any):
    total=0
    for j in any:
        if j%2==0:
            total+=j
    print(total)
sum_even(any)

lambda fun: it is a small anonymus function
this lambda functio can take n number of arguments but can only have one expression
syntax: lambda keyword (arguments):expression
'''
an = lambda a,b:a+b
an1 = lambda a,b:a-b
an2 = lambda a,b:a*b
an3 = lambda a,b:a/b
an4 = lambda a,b:a//b
an5 = lambda a,b:a**b
print(an(2,3))
print(an1(2,3))
print(an2(2,3))
print(an3(2,3))
print(an4(2,3))
print(an5(2,3))
