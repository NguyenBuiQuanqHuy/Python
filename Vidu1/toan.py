#Nhập 2 số nguyên dương m,n
#In ra tất cả số nguyên tố trong khoản [m,n]

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

n,m=1,50
for i in range(n,m+1):
    if isPrime(i): print(i,end=" ")