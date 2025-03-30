#Câu 1
# n=input("nhập chuỗi: ")
# chu_so=0
# chu_cai=0
# k=sum(1 for i in n if i.isalpha())
# for i in n:
#     if i.isalpha():
#         chu_cai+=1
#     if i.isdigit():
#         chu_so+=1
#
# d=n.upper()
# ds_tu=n.split()
# print(ds_tu)
# ky_tudb=len(n)-chu_so-chu_cai
# print("số lượng chữ số: ",chu_so,k)
# print("số lượng chữ cai: ",chu_cai)
# print("số lượng ký tư: ",ky_tudb)
# print("đảo ngược in hoa: ",d[::-1])

# #Câu 2
# n=list(map(int,input("Nhập n số nguyên: ").split()))
# while len(n)<=5:
#     n = list(map(int, input("Nhập lại n số nguyên: ").split()))
# tong_le=sum(x for x in n if x%2!=0)
# print("tổng lẻ:",sum(x for x in n if x%2!=0))
# print("thứ tự giảm dần:",sorted(n,reverse=True))
#
# tu_dien={x:n.count(x) for x in n}
# print(tu_dien)

#Câu 3
class Nguoi:
    def __init__(self,hoten,tuoi):
        self.hoten=hoten
        self.tuoi=tuoi

    def hien_thi(self):
        print( f"Họ tên: {self.hoten} - {self.tuoi} tuổi")

class SinhVien(Nguoi):
    def __init__(self,hoten,tuoi,mssv,diemtb):
        super().__init__(hoten,tuoi)
        self.mssv=mssv
        self.diem=diemtb

    def hien_thi(self):
        print( f"Họ tên: {self.hoten} - {self.tuoi} tuổi - {self.mssv} - {self.diem}")

n=int(input("Nhập n sinh viên: "))
while n<=2:
    n = int(input("Nhập lại n sinh viên: "))

dsSV=[]
for sv in range(n):
    hoten=input("Nhập tên: ")
    tuoi=int(input("Nhập tuôi:"))
    mssv=input("Nhập MSSV: ")
    diemtb=float(input("Nhập điểm TB: "))
    dsSV.append(SinhVien(hoten,tuoi,mssv,diemtb))

dsSV.sort(key=lambda sv:sv.diem,reverse=True)
for sv in dsSV:
    sv.hien_thi()