#1print 'softwarica' 10 times
for i in range(10):
    print('softwarica')
    
#2sum of a list
a=[2,3,4]
sum=0
for i in a:
    sum+=i
    
print(f'the sum of list is:{sum}')


# 3.print each character using indexing
a='anisha'
for i in range(len(a)):
 print(a[i]) 
 
      
#4 write a program to display integer from of a list. given list =[1,"a","c",2,3,4]
# a=1
# print(isinstance(a,str))  

a=[1,"a","c",2,3,4]
for i in a:
    if isinstance(i,int):
        print(i)
    

    
#5. multiplication of a each element. given list=[4,5,3,2]
a=[4,5,3,2]
product=1
for i in a:
    product*=i
        
print(f'the multiplication is:{product}')

# 6.multiplication table of a given number
a=5
for i in range(1,11):
    print(a,'*',i,'=',a*i)
    
#7. reverse a list 
reverse=[1,2,3,4,5]
for i in range(4,-1,-1):
  print(reverse[i])

#8 given list is [1,2,3,4] but expected output in new list [2,3,4,5]
a=[1,2,3,4]
new_list=[]  #initialize empty list
for i in a:
    new_list.append(i+1)  #append adds element to the list
print(new_list)


#9. Given list is lst=[1,2,3,4] but print 1 and 4 only 
a=[1,2,3,4]
for i in a :
    if i==1 or i==4 :
        print(i)

#10. Given list is lst=[1,2,3,4] but print 1 2 and 4 only 
b=[1,2,3,4]
for i in b:
    if i==1 or i==2 or i==4 :
        print(i)
        
#11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst = [1, 2, 3, 4]

for i in range(len(lst)):
    if lst[i] == 3:
        lst[i] = "a"

print(lst)

#12 Given list is [1,2,3,4,5] separate the elements into odd and even categories
num=[1,2,3,4,5]
odd=[]
even=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f'the even number is:{even}')
print(f'the odd number is:{odd}')

#13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
a=[1,2,3,'d',4,5,'a']
num=[]
char=[]
for i in a:
    if isinstance(i,int):
        num.append(i)
    else:
     if isinstance(i,str):
            char.append(i)
print(f'the integer is:{num}')
print(f'the string is:{char}')


# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

a=[1,2,3,4,'a','b']
num=[]
char=[]
for i in a:
    if isinstance(i,int):
        num.append(i)
    elif isinstance(i,str):
        char.append(i)
print(f'the integer is:{num}')
print(f'the string is:{char}')

#17. program to print the given number is odd or even
a=[2,3,4,5,6,7]
for i in a:
    if i%2==0:
        print(f'it is even number{i}')
    else:
        print(f'it is odd number{i}')


#9. Given list is lst=[1,2,3,4] but print 1 and 4 only 
a=[1,2,3,4]
for i in a :
    if i==2 or i==3 :
        continue
    else:
        print(i)

#17. program to print the given number is odd or even
a=3
for i in range(1):
    if i%2==0:
        print(f'it is even number{i}')
    else:
        print(f'it is odd number{i}')

