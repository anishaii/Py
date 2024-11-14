# #total of 22 marks
# # student_records=''
# # for i in range(2):
# #     name=input('enter your name')
# #     college_id=input('enter your college id')
# #     marks=input('enter your marks')
# #     student_records=f'{name},{college_id},{marks}' + '\n'
# # print(student_records)

# f=open('student.txt',mode='w')
# f.write('my name is anisha')
# f.close()

# f=open('abc.txt','w')
# f.write('accio')
# f.close()

 

# f=open('student.txt','w')
# lst=['1','2','3','4']
# f.writelines(lst)
# f.close()

f=open('student.txt','a')
f.writelines('shyam')
f.close()

#read methods
# f=open('student.txt')
# c=f.read(3)
# print(c)
# d=f.read(4)
# print(d)
# f.close() 

# f=open('student.txt')
# # c=f.readline(5)
# c=f.readline()
# print(c)

# # f=open('student.txt')
# # c=f.readlines(2)
# # print(c)

# # #imp*** (6 marks)
# # f=open('student.txt')
# # c=f.read()
# # f1=open('student1.txt',mode='w')
# # f1.write(c)
# # f.close()
# # f1.close()

# # with open('student.txt',mode='r') as f:
# # c=f.read()
# # print(c)
# # print(f.closed)

# # f=open('student.txt','w')
# # f.seek(8)
# # f.tell()
# # f.seek(6)
# # d=f.tell()
# # print(d)
# # print(c)
# # f.close()


#pickling/unpickling (10 marks)

# import pickle
# f=open('abc.txt','wb')
# lst=[1,2,3,4]
# pickle.dump(lst,f)
# f.close()


# import pickle
# f=open('abc.txt','rb')
# c=pickle.load(f)
# print(c)
# f.close()

import pickle
list=[1,2,3,4]
c=pickle.dumps(list)
a=pickle.loads(c)
print(a)
print(c)

#exception handeling: try except else finally
# import pickle
# f=open('hod.txt','wb')
# lst=[1,2,3,4]
# pickle.dump(list,f)
# f.close()

# import pickle
# lst=[1,2,3,4]
# lst2=[7,8,9]
# ickle=pickle.dumps(lst2)
# print(ickle)




