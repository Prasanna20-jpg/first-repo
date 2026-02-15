from cmath import sqrt
a=int(input())
b=int(input())
c=int(input())
d=(b**2)-(4*a*c)
sol1=(-b+sqrt(d))/(2*a)
sol2=(-b-sqrt(d))/(2*a)
print(sol1)
print(sol2)