# #Câu 1
#
# n=input("Nhập chuỗi")
# tudainhat=""
# for e in n.split():
#     if len(e) > len(tudainhat):
#         tudainhat=e
# print("TỪ dài nhất: ",tudainhat)
#
# print(n.strip())
# #bỏ ký tự đặc biệt
# n=' '.join(c if c.isalpha() or c.isspace() else '' for c in n)
# print(n)
# print(n.title())
# n=' '.join(n.split())
# print(n)
#
# chuoi=n.lower()
# for i in chuoi.replace(" ",""):
#     dem={c: chuoi.count(c) for c in set(chuoi)}
# print(dem)
from math import isqrt

# Câu 2
# n=list(map(int,input("Nhập danh sách : ").split()))
# while len(n)<=5:
#     n = list(map(int, input("Nhập lại danh sách : ").split()))
# scp=[]
# def soCP():
#     for i in n:
#         if i==isqrt(i)**2:
#             scp.append(i)
#     print(scp)
# soCP()

# Câu 3
class NhanVien:
    def __init__(self,ma_nv,hoten,luongcb):
        self.ma_nv=ma_nv
        self.hoten=hoten
        self.luongcb=luongcb

    def hienthi(self):
        print(f"{self.ma_nv}, {self.hoten}, {self.luongcb}")

class NhanVienSanXuat(NhanVien):
    def __init__(self,ma_nv,hoten,luongcb,so_sp):
        super().__init__(ma_nv,hoten,luongcb)
        self.so_sp=so_sp

    def hienthi(self):
        print(f"Mã NV: {self.ma_nv}, {self.hoten}, Lương: {self.luongcb}, Số sản phẩm: {self.so_sp}")

    def luong(self):
        return self.luongcb + self.so_sp *5000

class NhanVienVanPhong(NhanVien):
    def __init__(self,ma_nv,hoten,luongcb,so_ngay):
        super().__init__(ma_nv,hoten,luongcb)
        self.so_ngay=so_ngay

    def hienthi(self):
        print(f"Mã NV: {self.ma_nv}, {self.hoten}, Lương: {self.luongcb}, Số ngày làm việc: {self.so_ngay}")

    def luong(self):
        return self.luongcb * self.so_ngay*200000

n=int(input("Nhập số lượng nhân viên: "))
while n<=1:
    n = int(input("Nhập lại số lượng nhân viên: "))
dsnv=[]
for nv in range(n):
    ma_nv=input("Nhập mã nhân viên: ")
    hoten=input("Nhập tên nhân viên: ")
    luongcb=int(input("Nhâp lương cơ bản: "))
    choice=int(input("Chọn loại nhân viên - 1 or 2: "))
    if choice==1:
        print("\n Nhân viên sản xuất: \n")
        so_sp=int(input("Nhập số sản phẩm:"))
        dsnv.append(NhanVienSanXuat(ma_nv,hoten,luongcb,so_sp))
    if choice==2:
        print("\n Nhân viên văn phòng: \n")
        so_ngay=int(input("Nhập số ngày làm việc:"))
        dsnv.append(NhanVienVanPhong(ma_nv,hoten,luongcb,so_ngay))


dsnv.sort(key=lambda nv: nv.luong(),reverse=True)
for nv in dsnv:
    nv.hienthi()
    print(nv.luong())

