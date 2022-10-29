def p_f_s(num):
    pfs=0
    for i in range(1,num):
        if num%i==0:
            pfs +=i
    return pfs
    
a=int(input())
b=int(input())
if p_f_s(a)==b and p_f_s(b)==a:
    print("Amicable")
else:
    print("Not Amicable")