n=int(input("start no:"))
m=int(input("end no:"))

for i in range(n,m):
    if (i%2==0):
       print("even",i)
    else:
        print("odd",i)
