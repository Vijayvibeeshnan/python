#left shift
x,y=(int(i) for i in input().split())
if(1<=x)&(y<=1000):
    print(x<<y)
    
#find bitwise XOR array
N=int(input())
arr=list(map(int,input().split()))
a=arr[0]
for i in range(1,N):
    a=a^arr[i]
print(a)
