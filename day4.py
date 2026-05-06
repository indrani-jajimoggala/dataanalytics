'''
DATA TYPES :
DATA - Collection of information about particular item or personal details of the person.
they are two types of datatype - 1. Mutable datatype, 2. Immutable data type

1. Mutable Datatype
--> I can modify directly on the variable, which the data type have taken.
    example : list, dictionary
2. Immutable Datatype
--> Where can not be modified directly on the variable assign to the data type.
    example : int, string

Integer or int:
Storing the number or digit in the variable.
num = 9
print(num)

Float or float :
Storing decimal value in the variable is called float
num_2 = 12.45

String or str:
--> String is collection of char that are inclosed in '',"",''' '''
    Immutable Datatype. doesnot performance directly

String Methods :
----------------
replace() - This method is used to replace or change old sub-string with new string.
syntax: variable_name.replace("old_str","new_str")

eg : str = "python is programming language"
     print(str.replace("python","java"))
     print(str)
     o/p: java is programming language
          python is programming language
        
str = "python is programming"
print(str.replace(" ","-@"))

index():
-->index is used to get the particular substring, item from string, list and tuple by calling with index position
   if the substring is not found in index method, it will gives value error "substring is not found". and then execution will stops there.
syntax: print(variable_name.index('substr'))

print(str.index('o')) #4

find():
gives the position number of the element.
print(str.find('i'))  #7
priint(str.find('z')) #-1 (sudstring not found)

concatenation (+): A + acts as different way, if we are adding 2 integers it acts like addition in other cases such as list, str and tuple
it act like concatenation.
syntax: 
+ - addition while we are adding two numbers
+ - concatenation of two str, lst, tuple

str1 = "hlo"
str2 = "what's up"
print(str1+str2)

num=2
num1=3
print(num+num1)
'''
#split()
#This method is used separate the string using a substring and it will split into list such as before the substring is one index and after the substring is another index.
#syntax: variable_name.split("substring")
'''
print(str.split(" "))
print(str.split("is"))

#strip():
#This method is used to remove from 1st index position or form last index position.
print(str.strip("age"))


#join(): 
print("-".join(str))

count()- tells about how many times that particular letter is repeated in that string
casefold()
isalnum()
isalpha()
isdigit()
isdecimal()-not there
isupper()
islower()

num=int(input("enter a num:"))
print(num)
print(f"{num} is a even number") '''
'''
str = "python is programming"
str1 = "python123"
str3 = "123"
str4 = 12.4
str5 = "python is programming languages"

print(str.replace("python","java"))
print(str)
print(str.strip(" "))
print(str.strip("age"))
print("-".join(str))
print(str.count("a"))
print(str.count("i"))
print(str.index("p"))
print(str.rindex("p"))
print(str.find("y"))
print(str.find("z"))
print(str.rfind('i'))
print(str.isupper())
print(str.lower())
print(str.islower())
print(str.count('p'))
print(str.casefold())
print(str1.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str3.isnumeric())
print(str.endswith("programming"))
print(str.startswith("python"))
print(str+str1)
print(str1+str3)
print(str.zfill(30))


variables are nothing but storing the datatypes to access them to perform any operations.
input: int(input("enter a num: ") -- user input '''


a = ["i","am","ganesh"]
print(" ".join(a))
