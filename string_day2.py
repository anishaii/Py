a='programming'
b=a.center(13)
print (b)
  
a='program'
print(a.center(12,'*'))

a='python'
print (a.rjust(10,'*'))




a='python'
print(a.ljust(10,'*'))

a= 'python programming' #gap between two words
print ('python\tprogramming'.expandtabs(tabsize=10))

a='python'
print(a.find('P'))

a='python'
print(a.find('p'))



a='python'
print(a.rfind('p')-len(a))

a='python'
print(a.rindex("p"))

a= 'python programming' #first word letter in upper case
print (a.capitalize())

a= "python programming" #first and second word  letter in upper case
b= a.title()
print(b)

a= "python programming" #whole word in uppercase
b= a.upper()
print(b)

a= "Python Programming" 
b= a.lower()
print(b)

a='nike' 
b=a.islower()
print(b)

a='nike programming'
b=a.istitle()
print(b)

a='anc'
b=a.isalpha()
print(b)

a='abc123'
b=a.isalnum()
print(b)

a='123'
b=a.isdigit()
print(b)

a='\n'
b=a.isspace()
print(b)

a='a123'
b=a.isidentifier()
print(b)

a='123abc'
print(a.isidentifier())

a='python'
b=a.center(8,'*')
print(b)