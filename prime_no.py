lower_bound=int(input())
upper_bound=int(input())
for i in range(lower_bound,upper_bound+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)