n=int(input("enter no:"))
for k in range(0,n):
    for m in range(k+1):
        print("*",end="")
    print()
    
for i in range(n,0,-1):
    for j in range(i-1):
        print("*",end="")
    print()
num=1
for y in range(0,n):
    for x in range(y+1):
        print(num,end="")
        num=num+1
    print()

for o in range(n,0,-1):
    for p in range(o-1):
        print(num,end="")
        num=num-1
    print()



