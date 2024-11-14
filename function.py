#parameter=variable
#arguement=value, data


def name(a):
    print('my name is',a)
name('anisha')

#function without  argument and parameter
def name():
    a='abc'
    print(a) 
name()

#function with  argument and parameter
def num(a):
    b=5
    c=a+b
    print(c)
num(10)
    

def add (a,b): #parameter funtion defination
    print(a+b)
    print(a*b)
add(20,50)  #function call argument
add(20,30)

#types of Argument:

# 1.positional argument
def add(a,b):   #a=10 b=30
    print(a)
    print(b)
add(10,30)

def add(a,b):   #a=10 b=30
    print(a)
    print(b)
add(30,10)


#default argument
def add(a,b=30):   #a=10 b=30
    print(a)
    print(b)
add(10)

def add(a,b=30):  
    print(a)
    print(b)
add(10,100)

#To summarize, although the parameter b has a default value of 30, this default value is not used in this case because you provided
# an explicit value (100) when calling the function. The default value is only used if no argument is provided for b during
# the function call.

 
#keyword argument
def add(age,name):
    print(age,name)
add(name='ram',age=26)
#To summarize:
#Keyword arguments allow you to specify the values of the parameters by name, rather than by their position in the argument list.
#This means you can provide the arguments in any order, as long as you specify the parameter names.
#In this case, the function correctly identifies name as 'ram' and age as 26, and prints them in the order defined in the function.


print('hello')
def softwarica(a):
    print(a)
print('python')
softwarica(30)
print('abc')


#variable length argument

# def abc(a): takes only one potional argument 
#     print(a)
# abc(10,20,30)

def abc(*a): # *a syntax in the parameter means that a will collect all the positional arguments passed to the function into a tuple.
    print(a)
abc(10,20,30)
 



def abc(a,*args): # a takes positional value 10 while *args takes remainning value and gives answer in tuple
    print(args)
    print(a)
abc(10,20,30)

# def abc(*args,a): #args will collect all the positional arguments passed to the function into a tuple. leaving no argument
#positional value a
#     print(args)
#     print(a)
# abc(10,20,30)

def abc(*args,a): 

    print(args)
    print(a)
abc(10,20,30,a=50) #a=50 keyword argument

def abc(a,*args):
    print(args) #empty tuple
    print(a) #potional argument
abc(10)

#keyword variable length
def abc(**a): # **a syntax in the parameter means that a will collect all the keyword arguments passed to the function into a dictionary.
    print(a)
abc(a=20,b=30,c=40)

# def abc(*a,**a):  cannot use same variable
#     print(a)
# abc(a=20,b=30,c=40)
#positional argument cannot come after keyword arguments

def abc(*a,**b):
    print(a)
    print(b)
abc(4,5,a=20,b=30,c=40)

def abc(*a,**b):
    print(a)
abc(4,5,a=20,b=30,c=40)


a=[1,2,3,4]
def total_sum(a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)
total_sum([1,2,3,4])

fact=5
def factorial(fact):
    f=1
    for i in range(1,(fact+1)):
        f=f*i
    print(f)
factorial(5)


#print softwarica 10 times

def abc():
    for i in range(10): 
        print('softwarica')
abc()

#print each character using indexing
a='anisha'
def abc(a):
    for i in a:
        print(i)
abc('anisha')

# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
list=[1,'a','c',2,3,4]
def xyz(list):
    for i in list:
        if isinstance(i,int):
            print(i)
xyz([1,'a','c',2,3,4])


# multiplication of a each element. given list=[4,5,3,2]
list=[4,5,3,2]
def abc(list):
    a=1
    for i in list:
        a*=i
        print(a)
abc([4,5,3,2])
        