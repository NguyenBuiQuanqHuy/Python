class SinhVien:
    def __init__(self,maso,hoten,dsmh):
        self.maso=maso
        self.hoten=hoten
        self.dsmh=dsmh

    def diemTB(self):
        return sum(self.dsmh.values())/len(self.dsmh)

    def __str__(self):
        return f"{self.maso}-{self.hoten}-{self.diemTB():.2f}"

n=int(input("Nhập số lượng sinh viên: "))
# while n<=2 or n>=1000:
#     n=int(input("Nhập lại số lượng sinh viên: "))

dsSV=[]
for i in range(n):
    maso=input("Nhập mssv: ")
    hoten=input("Nhập tên sinh viên: ")
    ds_mon={}
    so_mon=int(input("Nhập số môn học: "))
    for j in range(so_mon):
        mon=input("Nhập tên môn học: ")
        diem=float(input(f"Nhập điểm {mon}: "))
        ds_mon[mon]=diem
    dsSV.append(SinhVien(maso,hoten,ds_mon))

print("\nDanh sách sinh viên:")
for i in dsSV:
    print(i)

dsSV.sort(key=lambda sv:sv.diemTB(),reverse=True)
for i in dsSV:
    print(i)

k=input("Nhập mssv cần tìm: ")
for sv in dsSV:
    if k==sv.maso:
        print(sv)
        break
    else:print("ko tìm thấy")