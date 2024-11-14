# a='hello'
# a='programming'
# print('a')

# a='aapython'
# print(a.count('a')) # checks the occurance of the character in string

# a='aapython'
# print(a.find('p')) #find method finds the index of the first occurance of the character and not found returns 0

# a='aapythoynn'
# print(a.rindex('y')) # last occure of the character and prints the index

# # a='aapytbhona'
# # print(a.center(10,'**'))#cannot use two fill char

# a='aapytbhona'
# print(a.center(15,'*'))

a='python'
print(a.center(19,'*'))

# a='python'
# print(a.ljust(19,'*')) #<-----------

# a='python'
# print(a.rjust(19,'*')) #--------->


# a='anisha124'
# print(a.isalnum()) #print true if it is alphabet and numeric but prints false if it contain space between character or contain special @#$

# a='anisha124'
# print(a.isalpha())  #is true if contains only alphabet and no numeric value space or special character


# a='aabc'
# b=a.replace('a','abc')
# print(b)

# a='aabc'
# b='a'.replace('a','abc')
# print(b)


# a='aabc'
# b=a.replace('w','abc')  #w is not found so it remains unchanges
# print(b)

# a='aabc'
# b='a'.maketrans('a','a')
# print(b)

# a='python'
# b=a.maketrans('thh','ABC')
# print(a.translate(b))

# a='python'
# b=a.maketrans('ABC','pyt')
# print(a.translate(b))
# #Since 'python' does not contain 'A', 'B', or 'C', no substitutions are made by the translation table. Hence, the string remains unchanged.

# a="Python Programming "
# print(a.istitle())


# print(a.isspace())


# i=25
# j=15
# k=17

# if i<j:
#     if j<k:
#         i=j
#     else:
#         j=k
# else:
#     if j>k:
#         j=i
#     else:
#         i=k
# print(i,j,k)

# a=1
# b='1'
# print(a is b)

# print("anisha","gc" ,sep=' ')

# a=4
# print(f'the number is {4}')

# a=1
# while  a<=5:
#     print('ninam')   
#     a=a+1
    
# a='ninam'  
# for i in a:
#     print(i)
    
# a='anisha'
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1
    
# a = 'ninam'
# i = 0

# while i < len(a):
#     print(a[i])
#     i += 1
    
    
# # sum=2
# # i=0
# # while i<10:
# #     print(i)
# #     i=i+1
# #     sum=sum+0
# # print(sum)

# sum=2
# for i in range(10):
#     print(i) 
#     sum+=0
# print(sum)4

# sum=1
# i=0
# while i<=5:
#     print(sum)
#     i=i+1
# print(i)

# a=[1,2,3,4,5]
# i=0
# sum=0
# while i <len(a):
#     sum=sum+a[0]
#     i=i+1
# print(sum) 

# a=5
# fact=1
# i=1
# while i<a:
#     fact=fact*i
#     i=i+1
#     print(fact)

# i=0
# while i<5:
#     print(i)
#     if i==3:
#         break
#     i=i+1
    
# i=1
# while i<3:
#     i=i+1
#     print(i)
#     if i==2:
#         break
    
# i=0
# while i<5:
#     i=i+1
#     print(i)
#     if i==2:
#         continue


#variable length argument

# def abc(a): takes only one potional argument 
#     print(a)
# abc(10,20,30)

# def abc(*a): # *a syntax in the parameter means that a will collect all the positional arguments passed to the function into a tuple.
#     print(a)
# abc(10,20,30)
 



# def abc(a,*args): # a takes positional value 10 while *args takes remainning value and gives answer in tuple
#     print(args)
#     print(a)
# abc(10,20,30)

# def abc(*args,a): #args will collect all the positional arguments passed to the function into a tuple. leaving no argument
# #positional value a
#      print(args)
#      print(a)
# abc(10,20,30)

# def abc(*args,a): 

#     print(args)
#     print(a)
# abc(10,20,30,a=50) #a=50 keyword argument

# def abc(a,*args):
#     print(args) #empty tuple
#     print(a) #potional argument
# abc(10)

#keyword variable length
# def abc(**a): # **a syntax in the parameter means that a will collect all the keyword arguments passed to the function into a dictionary.
#     print(a)
# abc(a=20,b=30,c=40)

# def abc(*a,**a):  cannot use same variable
#     print(a)
# abc(a=20,b=30,c=40)
#positional argument cannot come after keyword arguments

# def abc(*a,**b):
#     print(a)
#     print(b)
# abc(4,5,a=20,b=30,c=40)

# def abc(*a,**b):
#     print(a)
# abc(4,5,a=20,b=30,c=40)

# a='pythonprogramming'
# print(a.title())


# e='python\rab' 
# print (e)

# a=[3,6,8,9]
# sum=3
# for i in range(1,len(a)-1):
#     sum=sum+a[i]
# print(sum)

# print('hello'.capitalize())

A=[[1,2,3],[4,5,6],[7,8,9]]