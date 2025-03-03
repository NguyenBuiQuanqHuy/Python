# Viết ct tính tổng các số đã nhập, bấm 0 để dừng
tong = 0
while True:
    try:
        n=int(input("Nhập 1 số nguyên (Nhập 0 để dừng): "))
        if n == 0:
            break
        else:
            tong += n
    except:
        pass
print(f"Tổng các số đã nhập={tong}")
