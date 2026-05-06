'''
num = 5
for j in range(1,num+1):
    print("*")

num = 5
for i in range (1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

num = 5
for i in range (1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

num = 5
for i in range (num,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

num = 5
for i in range (num):
    for j in range(num-i-1,0,-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()
print("---------------------")
num = 5
for i in range (num,0,-1):
    for j in range(num-i-1,0,-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()
'''

# num1 = 5
# num2 = 6
# operator=int(input("\n1.add \n2.sub \n3.multi \n4.div \n5.power \n6.remainder: "))
# if operator == 1:
#     print("num1+num2:",num1+num2)
# elif operator == 2:
#     print("num1-num2:",num1-num2)
# elif operator == 3:
#     print("num1*num2:",num1*num2)
# elif operator == 4:
#     print("num1/num2:",num1/num2)
# elif operator == 5:
#     print("num1**num2:",num1**num2)
# elif operator == 6:
#     print("num1%num2:",num1%num2)
# num = 5
# for i in range (1,num+1):
#     for j in range(num-i,0,-1):
#         print("",end="")
#     for k in range(1,i+1):
#         print("* ",end="")
#     print()
num = 5 
for i in range(1,num+1):
    print(i)