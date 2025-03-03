def snt(n):
    factor=[]
    i=2
    while i * i <= n:
        while n%i==0:
            factor.append(i)
            n//=i
        i+=1
    if n>1:
        factor.append(n)
    return factor

numbers = list(map(int,input().split()))
thua_so={}
for i in numbers:
    thua_so[i]=snt(i)
print(thua_so)