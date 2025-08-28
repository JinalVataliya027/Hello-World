a=[]
n=int(input("How Many Number You Want You Enter="))
for i in range(n):
    x=int(input("Enter number="))
    a.append(x)

print("Current Array=",a)

n=len(a)
for i in range (0,n-1):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print("Sort Array=",a)
