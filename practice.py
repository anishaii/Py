#1
l = [10, 20, 30, 40, 50]  #list containing integers
t = ('Sundeep', 25, 79.58) # tuple containing float, integer and string
s = 'set theory' # string containing characters
#set conversion/ datatype conversion
s1 = set(l) 
s2 = set(t)
s3 = set(s) #When a string is converted to a set, each character in the string becomes an element of the set
print(s1)
print(s2)
print(s3) 


#2.  Given a list
#lst = [10, 25, 4, 12, 3, 8]
#How will you check whether 30 is present in the list or not?

lst=[10,25,4,12,3,8]

if 30 in lst:
    print('30 is present in list')
else:
    print('30 is not present in list')
    
#3.  Given input
#a=[1,2,3,4]
#expected output: [1,2,3,4,[8,9]]

a=[1,2,3,4]
a.append([8,9])
print(a)

#4.  Write a Python program to copy a list.ne
a=[2,4,6,8]
b=a.copy()
print(b)

# s = 'Hello'
#How will you obtain a list['H', 'e', 'l', 'l', 'o'] from it?

s = 'Hello' #string
#datatype conversion
l=list(s) 
print(l) #Each character in the string becomes an individual element in the list.

#6.  Suppose a list has 20 numbers. Write a program that removes all duplicates from this list.

 
