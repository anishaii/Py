# # #local variable

# # def add(a):
# #     b=10
# #     print(a+b)
# # add(20)

# # #global
# # a=10
# # def sum():
# #     b=19
# #     print(a)
# #     print(a+b)
# # sum()
# # print(a)

# # #identity operator
# # a=50
# # b=50
# # print(a is b)

# # a=[1,2,3]
# # b=[1,2,3]
# # print(a is b)

# # a=5
# # b='5'
# # print(a is not b)
# # #membership operation 
# # a='anisha'
# # print('i' in a)

# # a='ninam'
# # print('h' not in a)
# # #zfill
# # a='anisha'
# # print(a.zfill(10))
# # #center
# # a='anisha'
# # print(a.center(10,'*'))
# # #pop
# a={1:'a',2:'b',3:'c'}
# b=a.pop(2)
# print(b)   
# print(a)
# # #popitem
# # a={1:'a',2:'b',3:'c'}
# # b=a.popitem()
# # print(b)

# # #isprintable
# # p1='anisha'
# # p2='\n'
# # print(p1.isprintable())
# # print(p2.isprintable())

# # #isspace
# # s1='\t'
# # s2='hello world'
# # print(s1.isspace())
# # print(s2.isspace())

# # #variable length argument
# # def add(*args):
# #     print(args)
# # add(4,2,6)

# # def all(**kwargs):
# #     print(kwargs)
# # all(a=4,b=8,c=10)

# # #append
# # fruits=['appple','mange','banana']
# # fruits.append('orange')
# # print(fruits)

# # #extend
# # num=[1,2,3,4]
# # num.extend([5,6])
# # print(num)

# # #ljust
# # a='harrypotter'
# # print(a.ljust(15,'*'))

# # #rjust
# # b='hello'
# # print(b.rjust(10,'*'))

# # #discad
# # a={1,2,3,4}
# # b=a.discard(4)
# # print(a)

# # #clear
# # a={1,2,3,4}
# # b=a.clear()
# # print(a)

# # import time

# # def current_time():
# #     return time.ctime()
# # print(current_time)

# # #format method
# # a='anisha'
# # b=10
# # print('my name is {}. Iam {} years old '.format(a,b))

# # #maketrans

# # a='abcde'
# # b=a.maketrans('abc','ABC')
# # print(b)

# # def sum(a,b):
# #     print(a+b)
# # sum(2,4)


# # import time

# # def current_time():
# #     return time.ctime
# # print(current_time)

# # a='ani\tsha'
# # e_text=a.expandtabs(6)
# # print(e_text)

# # #map(function,iterable,...)

# # a=[1,2,3,4]
# # i=map(lambda x:x+2,a)
# # print(list(i))

# # #reduce(function,interable,[initializer])

# # from functools import reduce

# # # Use a lambda function to subtract numbers with an initializer
# # numbers = [1, 2, 3, 4, 5]
# # result = reduce(lambda x, y: x - y, numbers, 10)
# # print(result) 


# # s1={1,2,3,4}
# # s2={1,2,3,4,5}
# # print(s1.issubset(s2))

# # s1={1,2,3,4}
# # s2={1,2,3,4,5}
# # print(s1.intersection(s2))

# # s1={1,2,3,4}
# # s2={1,2,3,4,5}
# # print(s1.union(s2))

# # # Initialize a counter to keep track of lines that don't start with 'A'
# count = 0


# with open('aabc.txt', 'r') as file:
    
#     for line in file:
    
#         if not line.strip().startswith('A'):
#             count += 1


# print(f"Number of lines not starting with 'A': {count}")


# # # Initialize a counter for the word "is"
# # count = 0

# # # Open the file 'notes.txt' in read mode
# # with open('notes.txt', 'r') as file:
# #     # Read the file line by line
# #     for line in file:
# #         # Split the line into words
# #         words = line.split()
# #         # Count occurrences of "is" in each line (case insensitive)
# #         count += words.count("is") + words.count("Is") + words.count("IS")

# # # Display the result
# # print(f'The word "is" occurs {count} times in the file.')

# # a={'name':'anisha','age':19}
# # print(a)
# # a['name']='Ninam'
# # a['age']=20
# # a['name']=a.pop('name')
# # a['age']=a.pop('age')
# # print(a) 

# # a=[8,7,6,5,4,3,2,1]
# # sum=0
# # i=0
# # while i<8:
# #     sum=sum+a[i]
# #     i=i+1
# # print(sum)

# # a=[8,7,6,5,4,3,2,1]
# # sum=0
# # for i in range(len(a)):
# #     sum=sum+a[i]
# # print(sum)

# #assert
# a=10
# b=5
 
# assert b>a,'b is not greater than 10'

# print('this wont be printed because assertion fails')

# try:
#     1/0
# except ZeroDivisionError:
#     print('an error has occured')
#     raise
    

        
        
# def binary(list, search_item):
#     min = 0
#     max = len(list) - 1
    
#     while min <= max:
#         mid = (min + max) // 2
        
#         if list[mid] == search_item:
#             return mid
        
#         elif list[mid] > search_item:
#             max = mid - 1
        
#         else:
#             min = mid + 1
    
#     return -1
    
    
# def add(**args):
#     print(args)
# add(a=10,b=20,c=30)

# a='harry\tpotter'
# b=a.expandtabs(7)
# print(a)

# name='anisa'
# age=20
# print('my name is {}.iam {} years old'.format(name,age))

# a='abc'
# b=a.maketrans('abc','ABC')
# print(b)

# a={1,2,3,4}
# b=a.clear()
# print(a)

# a='anisha'
# print(a.ljust(8,'*'))

# a='hello world'
# b='\t'
# print(a.isspace())
# print(b.isspace())

# a='hello'
# b='hello\tworld'
# print(a.isprintable())
# print(b.isprintable())




# # Initialize the sum
# sum_of_odds = 0

# # For loop to iterate through the list
# for n in range(10):
#     if n % 2 != 0:  # Check if the number is odd
#         sum_of_odds += n  # Add it to the sum

# # Print the result
# print("The sum of all odd numbers in the list is:", sum_of_odds)

# sum=0
# i=0
# while i<10:
#     if n%2 !=0:
#         sum=sum+i
#         i=i+1
# print(sum)


# num = 10


# for i in range(2, num + 1):
    
#     is_prime = True

  
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break


#     if is_prime:
#         print(num)
        

# num=153
# sum=0
# temp=num

# while temp>0:
#     digit=temp%10
#     cube=digit**3
#     sum=sum+cube
#     temp//=10
    
# if sum==num:
    
#      print('it is armstrong')
# else:
#     print('it is not armstrong')
    
    
    
def binary(list, search_item):
    min = 0
    max = len(list) - 1
    
    while min <= max:
        mid = (min + max) // 2
        
        if list[mid] == search_item:
            return mid
        
        elif list[mid] > search_item:
            max = mid - 1
        
        else:
            min = mid + 1
    
    return -1
     