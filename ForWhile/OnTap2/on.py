#Số hoàn hảo
def SHH(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    return False

print(SHH(28))

#Ước chung lớn nhất của list
import math

n = list(map(int, input("Nhập danh sách số: ").split()))
max_uoc = n[0]  # Bắt đầu với số đầu tiên trong danh sách

for i in n[1:]:  # Duyệt từ phần tử thứ 2 trở đi
    max_uoc = math.gcd(max_uoc, i)  # Tính UCLN của max_uoc và số hiện tại

print("Ước chung lớn nhất:", max_uoc)


