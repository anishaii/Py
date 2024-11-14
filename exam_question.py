
#14. Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day

# a=int(input('enter for how many days you need a book'))
# if a<=5:
#     print(f'total:rs{a*2}')
# elif a<=6 and a<=10:
#     print(f'total:rs{a*3}')
# elif a<=11 and a<=15:
#     print(f'total:rs{a*4}')
# else:
#     print()
    

# if a<=5:
#     days_burrowed=a*2
# elif a<=10:
#     days_burrowed=(5*2)+(a-5)*3
# elif a<=15:
#     days_burrowed=(5*2)+(5*3)+(a-10)*4
# else:
#     days_burrowed=(5*2)+(5*3)+(5*4)+(a-15)*5
    
# print(days_burrowed)

# Accept input from user
# if given number is a multiple of both 3 and 5 prints "FizzBuzz" instead of number
# if  given number is a multiple of 3 but not 5 prints "Fizz" instead of number
# if given number is a multiple of 5 but not 3 prints "Buzz" instead of number
# if given number is not multiple of 3 or 5 prints value as usual. 

# num =int(input('enter any number'))

# if num %3 ==0 and num % 5==0:
#     print('FizzBuzz')
# elif num % 3 ==0:
#     print('Fizz')
# elif num % 5==0:
#     print('Buzz')
# else:
#     print(num)

#8.	removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"],
# string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython (36)

# bad_chars = [';', ':', '!', "*"]
# string = "py;th* o:n ! ;py * t*h:o !n"
# for i in bad_chars:
#     string=string.replace(i,'')
# print(string)


#5.	WAP to a check given num is Armstrong or not

# a=int(input('Enter a number:'))
# b=a//100
# c=(a//10)%10
# d=a%10
# e=b**3+c**3+d**323
# if a==e:
#     print(f'{a} in an armstrong')
# else:
#     print(f'{a}is not an armstrong')
    
#WAP to display all the prime numbers within a given range 
# a=int(input('enter a range number:'))
# print('list of prime number within a given range:')
# for i in range(a,a+1):
#     count=0
#     for y in range(1,i):
#         if i%y==0:
#             count+=1
#     if count==1:
#         print(i,end='')


#6.	WAP to check given num is Pallindrome or not
# a=int(input('enter a range number:'))
# a=str(a)
# if a==a[::-1]:
#     print(f'{a} is a pallindrome')
# else:
#     print(f'{a} is not a pallindrome')


#WAP python program to add a element in a tuple
# a=(1,2,3,5)
# b=list(a)
# b.append(4)
# print(tuple(b))

#WAP to rename  key and dict value
# a={'a':2}
# oldkey='a'
# newkey='A'
# a[newkey]=a.pop(oldkey)
# print(a)

#6.	Python program that accepts a string and calculate the number of digits and letters and space (15)
# a=input("enter a string:")
# digits=letters=spaces=0
# for i in a:
#     if i.isdigit():
#         digits+=1
#     if i.isalpha():
#         letters+=1
#     if i =='':
#         spaces+=1
# print('digits',digits)
# print('letters',letters)
# print('spaces',spaces)

#WAP to reverse a string using for and while loop
# a='anisha'
# for i in range(5,-1,-1):
#     print(a[i])
    
#2.	Write a Python script to concatenate following dictionaries to create a new one.( 14)
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#1.	A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that can be purchased. 
# The program should read three integers: the number of students in each of the three 


# user_input = input("Enter a string: ")

# letters_count = 0
# digits_count = 0
# index = 0

# # Use a while loop to iterate through the string
# while index < len(user_input):
#     if user_input[index].isalpha():
#         letters_count += 1
#     elif user_input[index].isdigit():
#         digits_count += 1
#     index += 1

# # Print the results
# print(f"Letters: {letters_count}")
# print(f"Digits: {digits_count}")

bad_chars = [';', ':', '!', '*']
string = "py;th* o:n ! ;py * t*h:o !n"

# Removing bad characters
for i in bad_chars:
    string = string.replace(i, '')

# Removing spaces
string = string.replace(' ', '')

print(string) 

a=1
b = 0


fibonacci_series = []


for i in range(25):
    
    a, b = b, a + b
    

    if 3 <= a <= 25:
        fibonacci_series.append(a)


print("Fibonacci series between 3 and 25 using for loop:", fibonacci_series)


a= 1
b = 0


fibonacci_series = []


while b <= 25:
 
    a, b = b, a + b
   
    if 3 <= a <= 25:
        fibonacci_series.append(a)


print("Fibonacci series between 3 and 25 using while loop:", fibonacci_series)

#WAP to rename  key and dict value
a={'a':2}
oldkey='a'
newkey='A'
a[newkey]=a.pop(oldkey)
print(a)


a=[1,2,3,4]
b=map(lambda x:x+1,a)
print(list(b))


bad_chars = [';', ':', '!', '*']
string = "py;th* o:n ! ;py * t*h:o !n"

for i in bad_chars:
    string=string.replace(i,'')
    
    string=string.replace(' ','')
print(string)


a={'name':'anisha','age':19}
print(a)
a['name']='ninam'
a['age']=20
a['name']=a.pop('name')
a['age']=a.pop('age')
print(a)

Numbers = [8, 7, 6, 5, 4, 3, 2, 1]
i=0
sum=0
while i<len(Numbers):
    sum=sum+Numbers[i]
    i=i+1
print(sum)

count = 0


with open('notes.txt', 'r') as file:
   
    for i in file:
       
        words = i.split()
       
        count += words.count("is") + words.count("Is") + words.count("IS")


print('The word "is" occurs is times in the file is',count)







        
        
limit = 10

for num in range(2, limit + 1):

    is_prime = True
    
  
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
 
    if is_prime:
        print(num)
        
        
limit = 10
num = 2

while num <= limit:
    is_prime = True
    i = 2
    
    # Check if num is divisible by any number from 2 to num - 1
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    
    # If the number is prime, print it
    if is_prime:
        print(num)
    
    # Move to the next number
    num += 1
    
