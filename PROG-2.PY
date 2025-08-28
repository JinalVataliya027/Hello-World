n=int(input("Enter n="))

for r in range(1,n+1):
    for s in range(n-r,0,-1):
        print(" ",end="")
    for c in range(1,r+1):
        print("*",end="")
    print()
