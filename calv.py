
print("Calculator \n 1.Add \n 2.Substract \n 3.Multiply \n 4.Divide")

ch=int(input("Enter Choice(1-4): "))
a=int(input("Enter A:"))
b=int(input("Enter B:"))

if ch==1:
    c=a+b
    print("Sum = ",c)
elif ch==2:
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    c=a*b
    print("Product = ",c)
elif ch==4:
    c=a/b
    d=a%b
    print("Quotient = ",round(c))
    print("remainder=",d)
else:
    print("Invalid Choice")
