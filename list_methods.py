#list
#syntax
#variable name=[square bracket]

a=[1,2,3,4]
a.append([5,4])
print(a)
a.extend([5,3])
print(a)

#a.insert(1,'ram')
a=[1,2,3,4]
a[1]='ram'
print(a)

a=[1,2,3,4]
a.remove(1)#element
print(a)

a=[1,2,3,4]
a.pop(1)#indexing
print(a)

a=[1,2,3,4,5,6]
a.pop(a[2])
print(a)

a=[1,2,3,4,5,6]
a.pop() #if empty by default remove last value
print(a)


a=[1,2,3,4,5,6]
b=a.pop() #if empty by default remove last value
print(b)

#copy
a=[1,2,3,4] 
b=a.copy()
print(b)

#tuple
a=(1,2,3,4)
b=list(a)
print(b) #[1,2,3,4]
b.insert(3,5)
print(tuple(b))

a={1,2,3,4} #no indexing and slicing in dict
a.add(5)
print(a)

a={1,2,3,4}
a.add(5) #remove first elelment
print(a)
a.pop()
print(a)

a={1,2,3,4} #set function
a.clear()
print(a)

a={1,2,3,4}
b={4,5,6}
c=a|b #union
print(c)

a={1,2,3,4}
b={4,5,6}
c=a&b #intersection
print(c)

a={1}  # set function
b={4}
c=a&b 
print(c)

a={1,2,3} 
b={4,2,3}
c=a-b  #difference  only a value
print(c)

a={1,2,3} 
b={4,2,3}
c=a^b  # both a and b  difference value
print(c)

a={1,2,3,4}
b={1,2,3,6}
c=a.isdisjoint(b)
print(c)


a={1,2,3,4}
b={1,2,3,6}
c=a.issubset(b)# left to right
c=a.issuperset(b)#right to left
print(c)

a={'a':1,'a':2} #no same key 
print(a)

a={'a':1,'b':2} 
a['c']=12
print(a)


a={'b':2,'a':2}
c=a.pop('b')
print(c)
a.popitem()

a={'b':2,'a':3}
c=a.get('c','python')
print(c)

a={'b':2,'a':3}
c=a.get('c')  #none
print(c)

a={'a':2}
oldkey='a'
newkey='A'
a[newkey]=a.pop(oldkey)
print(a)

# a={'a':2,'b':3,'c':4}
# for i in a.items(): #keys , values
#     print(i)
    
a={'b':2,'a':3}
c=a.get('c','python')
print(c)
       
       
a='anisha'
print(a.zfill(10))

num=[1,2,3]
num1=num.append(1)
print(num)

a={1,2,3,4,2}
a.discard(2)
print(a)

# sum=1
# for i in range(4):
#     sum=sum+3
# print(sum)

# sum=1
# i=0
# while i<4:
#     sum=sum+3
#     i=i+1
# print(sum)

def abc(**args):
    print(args)
abc(a=1,b=2,c=3)

# def add(y):
#     x=10
#     print(x)
#     print(x+y)
# add(20)

x=10
def add():
    a=10
    print(x)
    print(a)
add()
print('x',x)
print('a', a)

a={1,2,3,4}
b={2,7,4,5}
print(a.symmetric_difference(b))

my_list = [1, 2, 3, 4, 5]

# Insert an element at index 2
my_list.insert(5, 'a')

print(my_list)

