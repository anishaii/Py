
    
a='sofwarica'
for i in a:
    print(a)
    

    
a='python'
b=len(a)

for i in range(b):
    print(i,'=',a[i])
    
    
a='python'
j=0
for i in range(5,-1,-1):
    print(j,'=', a[i])
j= j+1

a=2
for i in range(1,11):
    print(a, '*',i,'=',a*i)
    
    
# classwork

# 1. print softwarica 10 times

for i in range(10):  # range(10) generate sequence of number form 0 t0 10
    print('softwarica')
    
# 2. print softwarica 10 time but expected output is :
#0=softwarica
#1=softwarica
#2=softwarica
#3=softwarica
#4=softwarica
#5=softwarica
#6=softwarica
#7=softwarica
#8=softwarica
#9=softwarica

for a in range(10):
    print (a,'=','softwarica') #the value of a is printed along with string '=' and 'softwarica'

# 3. given input is python and expected output is :
#p
#y
#t
#h
#o
#n


a='python' # string 'python' is assigned to variable a
for i in a:  #for loop iterates over each character in a and i variable takes the current value of a string
    print(i)
    
# 4 . given input is python and expected output is :
#0=p
#1=y
#2=t
#3=h
#4=o
#5=n
    
a= 'python' 
b=len(a) # len() is used to calculate the length of string and it is assingned to variable b

for i in range(b): # here b is the length of string 'python'so, range(b) produces sequence of of number which corresponds valid indices of string 
    print(i,'=',a[i]) # here i is current index iterated over loop ,a[i] retrieves the character at index i from the string a
  
                       
a='python' # direct method without assingning value to another variable
for i in range(len(a)):
    print(i,'=',a[i])
    
# 5. given input is python and expected output is :
#0=n
#1=o
#2=h
#3=t
#4=p
#5=y
a='python'
j=0  #This line initializes a variable j with the value 0. This variable will be used to keep track of the index of each character in the output.

 
for i in range(5,-1,-1): #(starting value, ending value, step value)
    print(j,'=',a[i])
    j=j+1 #After printing each character, j is incremented by 1. This ensures that the indices printed in the output increase sequentially from 0 to 5.

# multiplication table of given number
#user input=2
#output should be 2*1=1,.....
a=2
for i in range(1,11):
    print(a,'x',i,'=',a*i)

# multiplication table of given number
#user input=2
#output should be 2*10=20,.....
a=2
for i in range(10,-1):
     print(a,'x',i,'=',a*i)
    
    
a=2
for i in range(10,0,-1):
     print(a,'x',i,'=',a*i)
     
# multiplication of each element ,list=[4,5,3,2] expected ouput is 120

given_List=[4,5,3,2]
product=1

for i in given_List:
    product*=i
    
print(f'the output is:{product}')

number=5

a='programming'
for i in range(10,-1,-1):
    print(a[i])
    
a=5
factorial=1
for i in range(1,(a+1)):
    factorial*=i
print('the factorial is',factorial)

a=[1,2,3,4]
sum=0
for i in a:
    sum+=i
print('the sum is {}'.format(sum))




    
    