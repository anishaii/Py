print('programming'.center(12,'*'))

print('abc'.zfill(3))

a='apple'
b=a.replace('p','a')
print(b) 

a='programming'
print(a.rfind('m'))

a='pytthon'
print(a.rindex('t'))

user_input='pythonprogramming'
print(user_input.title())

i=0

while i<4:

    i=i+1

    if i==2:

        continue

    print(i)

else:

    print('while else')
    
i=0

while i<4:

    print(i)

    i=i+1

    if i==2:

        continue

else:

    print('while else')

i=0

while i<4:

    print(i)

    i=i+1

    if i==2:

        break

    i=i+1

else:

    print('while else') 
    
a=[3,7,9,13]

i=0

sum=3

while i<len(a):

    

    if i==2:

        sum=0

    sum=sum+a[i]

    i=i+1

else:

    print(sum) 
    
a=[3,7,9,13]

i=0

sum=3

while i<len(a):

    if i==2:

        sum=0

    sum=sum+a[i]

    i=i+3

else:

    print(sum) 