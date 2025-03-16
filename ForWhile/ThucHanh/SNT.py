def kt_snt(n):
    if n<2:
        return False
    elif n>=2:
        for i in range(2,n):
            if n%i==0: return False

        return True

print(kt_snt(50))


def snt(n):
    factor=[]
    for i in range(2,n):
        while kt_snt(i) and n%i==0:
            factor.append(i)
            n//=i
    if n>1:
        factor.append(i)
    return factor
    # i=2
    # while i * i <= n:
    #     while n%i==0:
    #         factor.append(i)
    #         n//=i
    #     i+=1
    # if n>1:
    #     factor.append(n)
    # return factor

numbers = list(map(int,input().split()))
thua_so={}
for i in numbers:
    thua_so[i]=snt(i)
print(thua_so)