a='softwarica'
i=0
while i < len(a):
    print(i,a[i])
    i=i+1
    
a=2
i=1
while i<11:
    print(a,'*','i','=',a*i)
    i=i+1
    
    
a=[1,2,3,4]
total_sum=0
for i in a:
    total_sum+=i
print(total_sum)

a=[1,2,3,4]
total_sum=0
i=0
while i<len(a):
    total_sum=total_sum+a[i]
    i=i+1
print(total_sum)
    
email=input('enter your email')
password=int(input('enter your password'))
i=1
while i<=3:
    email=input('enter your valid email')
    password