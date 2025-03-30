n=list(map(int,input().split()))
sum=0
for i in n:
    if i%2!=0:
        sum+=i
print(sorted(n,reverse=False  ))
print(sum)