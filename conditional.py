#write an if-else statement to check if a string starts with a certain character.
a=input('enter a name')
if a.startswith('p'):
    print(f'the string starts with {a}')
else:
    print(f'the string doestnot starts with{a}')
    

    
#create an if else structure to determine if a character is a vowel or a consonant
j=(input('enter a character'))
if (j=='a' or j=='e'or j=='i'or j=='o'or j=='u'):
    print(f'it is a vowel {j}')
else:
    print(f'it is a consonant {j}')
    
    
#write an if else statement to check if a number is divisible by 5 and 11 or not
    
j=int(input('enter a number'))

if j % 5 == 0 and j % 11== 0:
    print(f'the given number is divisible by 5 and 11 is {j}')
else:
    print(f'the given number is not divisible by 5 and 11 is  {j}')




#write an if else statement to determine if a given password is at least 8 characters long

p=input('enter your password')

if p>=8:
    print(f'the given password is 8 character long {p}')
else:
    print(f'the given password is not 8 character long {p} ')


p=input('enter your password:')

if len (p)>=8:
    print('the given password is 8 character long ')
else:
    print('the given password is not 8 character') 
    
#Write an if else statement to check if an email address contains '@' and'.'
a=input('enter your email address:')  
if '@'in a and '.' in a:
    print('contain')
else:
    print('donot containa')
    
    
#Write an if else statement to determine if character is a digit or not
a=input('enter a character')

if a.isdigit():
    print('it is a digit')
else:
    print('it is not a digit')
    
#write an if else statement to see if an input string is equals to given string hello

a=input('enter a string')
if a=='hello':
    print('the value is equal')
else:
    print('the value is not equal ')
    
#write a if else statement to find out if the given number is positve,negative or zero
a=int(input('enter a number'))

if a > 0:
    print('it is positive')
elif a < 0:
    print('it is negative')
else:
    print('it is zero')
    
#use if else to check if a list is empty or not

# WAP which accepts marks of four subjects and display total marks, percentage and grade    
a=input('enter marks of math:') 
b=input('enter marks of science:')  
c=input('enter marks of social:') 
d=input('enter marks of english:') 
total_marks = a+b+c+d

percentage=(total_marks/400)*100

if percentage>=90:
    print('your grade is A+')
    
elif percentage>=80:
    print('A') 
    
elif percentage>=70:
    print('B+')

elif percentage>=60:
    print('B')
    
elif percentage>=50:
    print('c+')
    
elif percentage>=40:
    print('c')

else:
    print('fail')


    
