def sayhi(name):
    print(f"{name}")

st="Hi"
sayhi(st)


def xep_loai(dtb):
    # Ràng buộc giá trị của đtb
    assert isinstance(dtb,float) and 0<=dtb<=10,"Điểm ko hợp lệ"
    return "Đạt" if dtb >=5 else "Không đạt"
xl=xep_loai(4.0)
print(xl)

#Hàm có nhiều tham số

def swap(a,b):
    return b,a

x,y=5,10
a,b=swap(x,y)
print(a,b)

def generate_values():
    yield "Hello"
    yield "Nha Trang"
    yield 79

results =generate_values()
for r in results:
    print(r)

def tong(*value):
    return sum([i for i in value if isinstance(i,int)])

sum=tong(1,2,3,4,'4',6)
print(sum)

#truyền đối số theo từ khóa
def student_info(**sv):
    print(f"MSSV:{sv['MSSV']}\tHoten:{sv['hoten']}\tDTB:{sv['dtb']}")

student_info(MSSV="64130854",hoten="Nguyễn Bùi Quang Huy",dtb=9.9)
student_info(hoten="Đồng Nguyên Quang",dtb=9.7,MSSV='64130269')