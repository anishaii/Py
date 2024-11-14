# a=[1,2,3]
# # a.append([4,5])
# a.append(4)
# print(a)

# a=[1,2,3]
# a.extend([6,7])
# # a.extend('2')
# print(a)

# i=[2,3,4,5] # it removes the desired element
# i.remove(5)
# print(i)

# i=[2,3,4,5] #insert
# i[3]='homelander'
# print(i)

a=[1,2,3,4,5] #pop remove index
a.pop(4)
print(a)

a=[1,2,3,4,5]
a.pop(a[2])
print(a)


# a=[1,2,3,4,5] #if pop argument is empty by default it removes last element
# a.pop()
# print(a)

# a=[1,2,3,4,5]
# b=a.copy()
# print(b)

# #tuple
# a=(1,2,3,4,5)
# b=list(a)
# print(b)
# b.insert(8,9)
# print(tuple(b))

# a=(1,2,3,4)
# b=list(a)
# print(b) #[1,2,3,4]
# b.insert(3,5)
# print(tuple(b))

a={1,2,3,4} #no indexing and slicing in dict
a.add(5)
print(a)

# a={1,2,3,4}
# a.add(5) #remove first elelment
# print(a) #set take no argument
# a.pop()
# print(a)

# a={1,2,3,4}#set function
# a.clear() #clears all the element
# print(a)

# a={1,2,3,4}
# b={4,5,6}
# c=a|b
# print(c)

# a={1,2,3,4}
# b={4,5,6}
# c=a&b 
# print(c)

# a={1}  # set function
# b={4}
# c=a&b 
# print(c)

# a={1,2,3} 
# b={4,2,3}
# c=b-a 
# print(c)

# a={1,2,3} 
# b={4,2,3}
# c=a^b 
# print(c)

# a={1,2,3,4} #The isdisjoint() method checks whether two sets have no elements in common. 
# b={6,7,8}
# c=a.isdisjoint(b)
# print(c)

# a={1,2,3,4,6}
# b={1,2,3,6}
# # c=a.issubset(b)
# c=a.issuperset(b)
# print(c)

# a={'a':1,'a':2} # cannot have duplicate key and overwrite
# print(a)

# a={'a':1,'b':2}
# a['c']=3 #adding key and value
# print(a)

a={'b':2,'a':2}
c=a.pop('b')
print(a)
print(c)

# # print(c)
# a={'b':2,'a':2}
# c=a.popitem()
# print(a) #list 
# print(c) #tuple

# a={'b':2,'a':3,'c':4} #get  retrieve the value associated with the key
# c=a.get('c','python')
# print(c)

# a={'b':2,'a':3}
# c=a.get('c')  #none
# print(c)

# # a={'a':2}
# # oldkey='a'
# # newkey='A'
# # a[newkey]=a.pop(oldkey)
# # print(a)

# a={'a':2,'b':3,'c':4} # i is tuple item() gives key value pair
# for i in a.items():
#     print(i)

import pickle

# f=open('ijk.txt','wb')
# dic={'sita':1,'gita':2}
# pickle.dump(dic,f)
# f.close()

f=open('ijk.txt','rb')
a=pickle.load(f)
print(a)
f.close()

list=[16,17,18,19,20]

def linear_search(list,ram):
    for i in range(len(list)):
        if list[i]==ram:
            return i
    return -1

index=linear_search(list,20)
print(index)

#binary


def binary(list, search_item):
    min = 0
    max = len(list) - 1
    
    while min <= max:
        mid = (min + max) // 2
        
        if list[mid] == search_item:
            return mid  
        
        elif list[mid] > search_item:
            max = mid - 1
        
        else:
            min = mid + 1
    
    return -1