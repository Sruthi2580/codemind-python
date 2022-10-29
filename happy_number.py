n=int(input())
sume=0
ans=n
s=len(str(n))
while s>1:
    n=ans
    sume=0
    while n>0:
        s1=n%10
        n=n//10
        sume+=(s1*s1)
    ans=sume
    s=len(str(sume))
if ans==7 or ans==1:
    print(True)
else:
    print(False)
    