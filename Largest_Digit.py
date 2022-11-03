n=int(input())
c=[]
while n>0:
    r=n%10
    c.append(r)
    n=n//10
print(max(c))