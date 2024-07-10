def greetings():                        # function in python
    print('Welcome to AmarVerse')

greetings()                             # function calling

def details(name,age):
    print('Welcome '+name+' and you are '+str(age)+ ' years old')

details('Amar',22)

def details(name,age):
    print('Welcome '+name+' and you are '+str(age)+ ' years old')

details(name = 'Amar', age = 22)

def details(name,age):
    print('Welcome '+name+' and you are '+str(age)+ ' years old')

name = input('Enter your name: ')
age = input('enter your age: ')
details(name, age)

def fun(*names):                   # when * is used, it is going to have multiple values like tuple
    print('Hi '+names[1])          # have to use index number to access from multiple values

fun('Amar', 'Teja', 'Koteswari')

def add(num1, num2):
    return num1+num2
num1 = int(input('Enter num1: ')) #if you dont specify int then it will consider it as string 
num2 = int(input('Enter num2: ')) 
print(add(num1,num2))