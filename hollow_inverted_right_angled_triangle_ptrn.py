n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==1 or i==n or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    