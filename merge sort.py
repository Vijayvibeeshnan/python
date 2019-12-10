#merge sort
d=[1,2,3,4,8,6,67,34,23,78,9]
e=len(d)//2
a=d[:e]
a.sort()
print(a)
b=d[e:]
print(b)
b.sort()
c=a+b
print(c)
