class SinhVien:
    # Hàm thiết lập: constructor
    def __init__(self,mssv,hoten,dtb):
        self.mssv=mssv
        self.hoten=hoten
        self.dtb=dtb
    # Hàm in thông tin
    def print_info(self):
        print(f"mssv:{self.mssv}\tHọ tên:{self.hoten}\tĐTB:{self.dtb}")


sv1=SinhVien("64130854","Huy",7.5)
sv1.print_info()