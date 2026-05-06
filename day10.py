'''
while:
while statement will keep on executing until unless condition becomes true '''
'''
v = 1
while v <=5:
    print(v)
    v += 1
'''

'''
for:
range(): it will generate sequence of numbers upto limit.
syntax: range(start,stop,step)
'''
'''
choice_u = int(input("enter the limit: "))
for j in range(10, choice_u+1,3):
    print(j)
'''
'''
for i in range(2,20):
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
'''
'''
n = 8
for i in range(2,20):
    if n%i==0:
        print(f"{i} is not prime")
    else:
        print(f"{i} is prime")
'''
'''
break:
it will exist if the condition becomes true, and never enters into next loops
'''
'''
any = ["gani","san","sai","ani"]
for i in any:
    print(i)
    if i =="sai":
        print(i)
'''
'''
continue:
it will skip that particular iteration and goesto next iteration'''
'''
any = ["gani","san","sai","ani"]
for i in any:
    if i =="sai":
        continue
    print(i)
'''

'''
pass: it is space holder, holds the space not to get any error'''
'''
a = 9
b =90
if a>=b:
    pass
'''

n = 7
for i in range(2,8):
    if i%n==0:
        print(f"{i} is prime")
    else:
        print(f"{i} is not prime")
'''
num = int(input("enter a number: ")
count = 0
for an in range(1,num+1):
    if num%an == 0:
          cout+=1
if cout == 2:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

'''
nestd loop:
a loop inside the loop is called nested loop
'''
for j in range(2,100):
    count = 0
    for an in range(1,j+1):
        if j%an == 0:
            count+=1
    if count == 2:
        print(f"{j} is prime")
    else:
        print(f"{j} is not prime")
