#bubble sort
a=[1,6,3,4]
b=len(a)
for j in range(0,b):
    for i in range(0,b):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            print(a)
