#for formatting date
print('06','05','2024',sep='/') 

#
print('hello')
print('python')

print('hello',end='  ')
print('python')

print('hello',end='yyyyyy')
print('python')


a=20
b=30
c=a+b
print('the sum of a and b is {}'.format(c))

#indexing
a=20
b=30
c=a+b
print('{0} {1}'.format(20,30))

#by default indexing
a=20
b=30
c=a+b
print('{0} {1}'.format(20,30))

a=20
b=30

c=a+b
print('{0} {1}'.format(20,30))



# note: in f string you cannot pass agruments or value
a='aapython'
print('a'.find('a'))