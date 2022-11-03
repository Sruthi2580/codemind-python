n=int(input())
l=len(str(n))
m=n*n
l_d=m%pow(10,l)
if l_d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
