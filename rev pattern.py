n=int(input("enter no:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
for k in range(1,n):
    for m in range(0,k+1):
        print("*",end="")
    print()
    
