a,b=map(int,input().split())
i=max(a,b)
while True:
    if i%a==0 and i%b==0:
        print(i)
        break
    i+=1