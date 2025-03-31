
#
# n=input("Nhập chuỗi: ").strip().lower()
# tan_so={}
# for j in n:
#     if j in tan_so:
#         tan_so[j]+=1
#     else: tan_so[j]=1
# print(tan_so)

#Câu 2
n=list(map(int,input("Nhập: ").split()))
k=[]
for i in n:
    if i not in k:
        k.append(i)
k.sort(reverse=True)

print(k)
print(sum(filter(lambda x: x%2==0,k)))