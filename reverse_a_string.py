str=input()
left=0
n=len(str)
right=n-1
str=list(str)
while left<right:
    str[left],str[right]=str[right],str[left]
    left+=1
    right-=1
str="".join(str)
print(str)
