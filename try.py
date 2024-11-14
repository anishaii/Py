# def add(a):
#     b=10
#     print(a)
#     print(a+b)
# add(20)


# a=10
# def sum():
#     a=10
#     b=20
#     print(a)
# sum()
# print(a)

# a='anisa'
# print('a'  not in a)

# a=4
# b=4
# print(a is not b)

# a={1:'a',2:'b',3:'c'}
# b=a.pop(3)
# print(a)


# try:
#     1/0

# except ZeroDivisionError as e:
    
#     print('error occur')
#     raise

a=[16,17,18,19]

def linear_search(a,ram):
    for i in range(len(a)):
        if a[i]==ram:
            
            return i
    return -1
index=linear_search(a,19)
print(index)

a = 0
b = 1

fibonacci_series = []

for i in range(25):
    a, b = b, a + b

    if 3 <= a <= 25:
        fibonacci_series.append(a)

print("Fibonacci series between 3 and 25 using for loop:", fibonacci_series)