# a="123python"
# print(a.zfill(10)) # it gives error because zfill doesn't take two arguments

# a="123python"
# b=a.isidentifier()
# print(a) #it gives 123python because we are printing a 

a="python\n"
b=a.isprintable()
print(b) 

a=" "
b=a.isspace()
print(b) 

a="PythonProgramming Ho"
b=a.istitle()
print(b) 