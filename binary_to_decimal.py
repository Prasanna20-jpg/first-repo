def btod(n):
    res=0
    p2=1
    for i in range(len(n)-1,-1,-1):
        if(n[i]=='1'):
            res+=p2
        p2*=2
    return res
n="0111"
print(btod(n))