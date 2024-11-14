# 1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a=input('enter a first number')
b=input('enter a second number')

if a==b:
    print('1')
elif a>b:
    print('2')
else:
    print('3')
    
# 2.  Print "Hello" if a is equal to b, or if c is equal to d.  
  
a=input('enter a first number')
b=input('enter a second number')
c=input('enter a third number')
d=input('enter a fourth number')

if a==b or c==d:
    print('Hello')
else:
    print('they are not equal')


#3. Print "Hello" if a is equal to b, and c is equal to d.
a=input('enter a first number')
b=input('enter a second number')
c=input('enter a third number')
d=input('enter a fourth number')

if a==b and c==d:
    print('hello')
else:
    print('they are not equal')


#4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

x=int(input('enter a integer'))

if x>0:
    print('true')
elif x<0:
    print('false')  
else:
    print('zero')
    
    
#5. Check whether the user input number is even or odd and display it to user.
a=int(input('enter a number:'))

if a%2==0:
    print('it is even number')
    
else:
    print('it is odd number')
        
        
#WAP which accepts marks of four subjects and display total marks, percentage and grade.
#Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –> pass, 
#less than 40 –> fail
a = float(input("Enter marks of subject 1: "))
b = float(input("Enter marks of subject 2: "))
c = float(input("Enter marks of subject 3: "))
d = float(input("Enter marks of subject 4: "))

# Calculate total marks
total_marks = a + b + c + d

# Calculate percentage
percentage = (total_marks / 400) * 100

# Assign grade based on percentage
if percentage >= 70:
    print('Distinction')
elif percentage >= 60:
    print('first division')
elif percentage >= 40:
    print('pass')

else:
    print('fail')

# Display total marks, percentage, and grade
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}")


age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))

if age1>age2 and age1>age3 and age1>age4:
    print('age1 is the oldest')
elif age2>age1 and age2>age3 and age1>age4:
    print('age2 is the oldest')
elif age3>age1 and age3>age2 and  age3>age4:
    print ('age3 is oldest')
else:
    print('age4 is oldest ')
    
    
    # Accept ages of 4 people
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))

# Compare ages to find the youngest
if age1 < age2 and age1 < age3 and age1 < age4:
    print('age1 is youngest')
elif age2 < age1 and age2 < age3 and age2 < age4:
    print('age2 is youngest')
elif age3 < age1 and age3 < age2 and age3 < age4:
    print('age 3 is youngest')
else:
    print('age4 is youngest')
    
# Write a Python program to display your details like name, age, address in three different lines.

name=input(('enter your name:'))
age=int(input('enter your age:'))
address=input('enter your address:')

print(name)
print(age)
print(address)

#Write a python program which accepts the radius of circle from user and compute the area.

r=float(input('enter the radius:'))
aoc=3.15*r**2
print(aoc)

