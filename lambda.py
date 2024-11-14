b=lambda :print('hello')
print(b)


b=lambda :print('hello')
print(b)
b.__doc__ = 'aaaa'
print(b.__doc__)

a=lambda x,y :x+y
print(a(10,20))

a=lambda x,y :x+y
d,e=(a(10,20))
print(d)

# map (fundtion, iterable)

student_head=[2,4,8,6]
b=list(filter(lambda x:x+2,student_head))
print(b)

filter
a=[1,0,1,2,True,False]
b=list(filter(None,a))
print(b)

import datetime
b=datetime.datetime.now()
print(b.year)

import datetime
b=datetime.datetime.now()
c=b-datetime.timedelta(weeks=3)
print(c)

import math
print(math.floor(1.0))
print (math.ceil(2.1))
print (math.pow(2,3))
print (math.sqrt(4))
print (math.factorial(5))
print (math.fabs(5))


import random #0-1 ko value
print(random.random())
print(random.randrange(1,6)) #2
print(random.randint(1,6))
print(random.uniform(1,6))


a=[1,2,3,4]
random.shuffle(a)
print(a)



import random
a=[1,2,3,4]
random.seed(5)
print(random.choice(a))

