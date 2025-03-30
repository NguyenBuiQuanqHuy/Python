n=input("Nhập chuỗi: ")
n_hoa=n.upper()
num=sum(1 for c in n if c.isdigit())
n_nguoc=n[::-1]
print("chuỗi viết hoa:",n_hoa)
print("số ký tự số: ",num)
print("Chuỗi ngược:",n_nguoc)